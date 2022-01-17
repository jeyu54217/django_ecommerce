from django import forms
from orders.models import Order_Info


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order_Info
        fields = [
            'name',
            'email',
            'address',
            'postal_code',
            'city'
        ]
