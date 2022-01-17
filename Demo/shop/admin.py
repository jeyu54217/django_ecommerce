
from django.contrib import admin
from shop.models import (
    Category_A, 
    Category_B, 
    Product,
    )

class Category_A_Admin(admin.ModelAdmin):
    list_display=['name', 'slug' ] 
    prepopulated_fields = {'slug': ('name',)} # repeat field

class Category_B_Admin(admin.ModelAdmin):
    list_display=['name', 'slug'] 
    prepopulated_fields = {'slug': ('name',)} # repeat field

class Product_Admin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'price',
        'stock',
        'available',
        'created_at',
        'updated_at'
    ]
    list_filter = [
        'available',
        'created_at',
        'updated_at'
    ]
    list_editable = [
        'price',
        'stock',
        'available'
    ]
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Category_A, Category_A_Admin)
admin.site.register(Category_B, Category_B_Admin)
admin.site.register(Product, Product_Admin)



# Admin self-define actions : https://hakibenita.com/things-you-must-know-about-django-admin-as-your-app-gets-bigger
# The Django admin site : https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#module-django.contrib.admin
