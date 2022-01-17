from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path('alluth/', include('allauth.urls')), # 3rd-Party Login
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
    
]


"""
1. path(name)
2. include(namespace)
"""