
from django.shortcuts import render, get_object_or_404
from shop.models import (
    Category_A, 
    Category_B, 
    Product,
    )
from cart.forms import CartAddProductForm
from cart.cart_ import Cart  

# Variables for Rendering
categories_A = Category_A.objects.all() # Django models API -> DRF RESTful API
categories_B = Category_B.objects.all() 


def homepage(request):
    cart = Cart(request)
    return render(
        request,
        "homepage.html",
        { 
        'categories_A': categories_A,
        'categories_B': categories_B, 
        'cart': cart,  
        }
    )

def product_list(request, category_slug=None):
    category_B_slug = None
    products_by_slug = Product.objects.filter(available=True)
    cart = Cart(request)
    if category_slug:
        category_B_slug = get_object_or_404(Category_B, slug=category_slug)
        products_by_slug = products_by_slug.filter(category_B=category_B_slug)
    return render(
        request,
        'product/product_list.html',
        {
         'categories_A': categories_A,
         'category_B_slug': category_B_slug,
         'categories_B': categories_B,
         'products_by_slug': products_by_slug,
         'cart': cart,
        }
    )
## Searching Box ##
def product_search(request):
    cart = Cart(request)
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__contains=query) # Django Search : https://docs.djangoproject.com/en/4.0/topics/db/search/#search
        # Result exist
        if products.count() > 0 :
            return render(
                request,
                'product/product_list.html',
                {
                    'categories_A': categories_A,
                    'categories_B': categories_B,
                    'cart': cart,  
                    'products_by_slug': products,
                    'query': query
                }
            )
        # No Results
        else:
            return render(
                request,
                'product/search_NoResult.html',
                {
                    'categories_A': categories_A,
                    'categories_B': categories_B,
                    'cart': cart,
                }
            )
    # Empty Search
    else:
        return render(
            request,
            'product/search_NoResult.html',
            {
                'categories_A': categories_A,
                'categories_B': categories_B,
                'cart': cart,
            }
         )

def product_detail(request, id, slug):
    product = get_object_or_404(
            Product,
            id=id,
            slug=slug,
            available=True
        )
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    return render(
        request,
        'product/product_detail.html',
        {
        'categories_A': categories_A,
        'categories_B': categories_B,
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart,  
        }
    )

# QuerySet API reference() : https://docs.djangoproject.com/en/3.2/ref/models/querysets/#queryset-api-reference
# shortcut functions(render) :　https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#module-django.shortcuts
