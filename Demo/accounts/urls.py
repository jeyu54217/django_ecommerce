from django.urls import path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

# For Navbar Rendering
from shop.models import Category_A, Category_B
categories_A = Category_A.objects.all() 
categories_B = Category_B.objects.all()
context = {
    'categories_A': categories_A,
    'categories_B': categories_B,
    }

urlpatterns = [
    path('', accounts_views.profile, name='profile'),
    path('sign_up/', accounts_views.sign_up, name='sign_up'),
    path('login/',auth_views.LoginView.as_view(extra_context=context),name='login'),
    path('logout/',auth_views.LogoutView.as_view(extra_context=context),name='logout'),
    
]

# Custom LoginView : as_view(extra_context{"tag":Var}) :https://stackoverflow.com/questions/55107971/custom-loginview-django-extra-context