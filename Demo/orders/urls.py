from django.urls import path
from orders import views


urlpatterns = [
    path('create/',views.order_create,name='order_create'),
    path('finished/',views.order_finished,name='order_finished'),
    path('confirmed/',views.order_confirmed,name='order_confirmed'),



]
