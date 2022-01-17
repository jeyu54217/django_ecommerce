
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm
from accounts.tasks import send_email

# For Navbar Rendering
from django.shortcuts import render
from shop.models import Category_A, Category_B
from cart.cart_ import Cart
categories_A = Category_A.objects.all() 
categories_B = Category_B.objects.all()


@login_required
def profile(request):
    cart = Cart(request)
    return render(
        request,
        'account/account_profile.html',
        { 
        'cart': cart,
        'categories_A': categories_A,
        'categories_B': categories_B,   
        }
    )
    

def sign_up(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Save form but not commit to Database
            new_user = user_form.save(commit=False)
            # set password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Send Success Email 
            send_email.delay(new_user.email)
            
            return render(
                request, 
                'registration/register_done.html', 
                {
                'new_user': new_user,
                'categories_A': categories_A,
                'categories_B': categories_B, 
                }
           )
    else:
        user_form = UserRegistrationForm()
    return render(
        request, 
        'registration/register.html', 
        {
            'user_form': user_form,
            'categories_A': categories_A,
            'categories_B': categories_B, 
        }
    )