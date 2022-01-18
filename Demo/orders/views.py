
from orders.forms import OrderCreateForm
from orders.models import Order_Item
from orders.tasks import send_email
from django.shortcuts import render
from cart.cart_ import Cart
 # ECPay
from .create_order_Credit import *
from django.http  import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# For Navbar Rendering
from shop.models import Category_A, Category_B
categories_A = Category_A.objects.all() 
categories_B = Category_B.objects.all()

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                Order_Item.objects.create(
                    order_info=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            try:
                order_params = {
                    'MerchantTradeNo': datetime.now().strftime(f"NO%Y%m%d{order.id}"),
                    'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                    'PaymentType': 'aio',
                    'TotalAmount': int(cart.get_total_price()),
                    'TradeDesc': 'Test',
                    'ItemName': 'Product',
                    # 'ReturnURL': f'https://{settings.WEBSITE_URL}/orders/confirmed',
                    'ReturnURL': 'http://127.0.0.1:8000/orders/confirmed/',
                    'ChoosePayment': 'Credit',    
                    'ClientBackURL': f'https://{settings.WEBSITE_URL}/orders/finished/',
                    # 'OrderResultURL': f'https://{settings.WEBSITE_URL}/orders/finished',
                    'OrderResultURL': 'http://127.0.0.1:8000/orders/finished/',
                    'EncryptType': 1,
                }
                # 產生綠界訂單所需參數
                final_order_params = ecpay_payment_sdk.create_order(order_params)
                # 產生 html with form 
                action_url = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'  # 測試環境
                # action_url = 'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5' # 正式環境
                html = ecpay_payment_sdk.gen_html_post_form(action_url, final_order_params)
                send_email.delay(order.email , order.id)
                return HttpResponse(html)
            
            except Exception as error:
                 print(f"An exception happened: {error}")


    else:
        form = OrderCreateForm()
        return render(
            request,
            'order/order_create.html',
            {
                'form': form,
                'cart': cart,
                'categories_A': categories_A,
                'categories_B': categories_B,
            }
        )
        
        
# Confirm message to ECPay
@csrf_exempt
def order_confirmed(request):
    return 1|OK
    
# Return page to Client
@csrf_exempt
def order_finished(request):
    cart = Cart(request)
    cart.clear()
    return render(
        request,
        'order/order_created.html',
        {
        'cart': cart,
        'categories_A': categories_A,
        'categories_B': categories_B,
        }
    )