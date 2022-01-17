from django.contrib import admin
from orders.models import Order_Info, Order_Item


class OrderItemInline(admin.TabularInline):
    model = Order_Item
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'address',
        'postal_code',
        'city',
        'created_at',
    ]
    list_filter = [
        'created_at',
    ]
    inlines = [OrderItemInline]


admin.site.register(Order_Info, OrderAdmin)
