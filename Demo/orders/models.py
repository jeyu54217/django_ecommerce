from django.db import models
from shop.models import Product
from django.utils import timezone
from decimal import Decimal

class Order_Info(models.Model):
    name = models.CharField(
        max_length=50,
        default="Guest_01",
        )
    email = models.EmailField(
        default="jeyu54217@gmail.com",
    )
    address = models.CharField(
        max_length=250,
        default="address",
        )
    postal_code = models.CharField(
        max_length=20,
        default="000",
        )
    city = models.CharField(
        max_length=100,
        default="TPE",
        )
    created_at = models.DateTimeField(
        default = timezone.now
        )
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return int(sum(item.get_cost() for item in self.items.all()))


class Order_Item(models.Model):
    order_info = models.ForeignKey(
        Order_Info,
        related_name='items',
        on_delete=models.CASCADE
        )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
        )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    quantity = models.PositiveIntegerField(
        default=1
        )

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return int(self.price) * int(self.quantity)
  