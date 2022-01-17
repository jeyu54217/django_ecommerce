from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from cart.cart_ import Cart 
from cart.forms import CartAddProductForm

# For Navbar Rendering
from shop.models import Product,Category_A,Category_B
categories_A = Category_A.objects.all() 
categories_B = Category_B.objects.all()

@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request): 
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                    initial={
                        'quantity': item['quantity'],
                        'update': True
                    }
                )
    return render(
        request,
        'cart/cart_detail.html',
        {
            'cart': cart,
            'categories_A': categories_A, 
            'categories_B': categories_B, 
        }
    )
