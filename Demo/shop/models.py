from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category_A(models.Model):
    name = models.CharField(
        max_length=200,
        )
    slug = models.SlugField(
        max_length=200, 
        unique=True           
        )
    class Meta:
        ordering = ("name",)
        verbose_name = 'catgory_A'
        verbose_name_plural = 'categories_A'
        # why use verbose_name option? - To deal with the "s": https://1drv.ms/u/s!ArgTHAPiuIGQgcpJuzR5aAAhM6DNvg


    def __str__(self):
        """
        1. To display an object in the Django admin site  
           and as the value inserted into a template when it displays an object
        2. About  __str__method in Django : https://docs.djangoproject.com/en/3.2/ref/models/instances/#str
        """
        return self.name


class Category_B(models.Model):
    """
    About the hidden PK(id) field:
    1.The real database table for Category_B model will have a "category_A_id" column. 
    2.check : migrations/00xx_initial.py
    3.See also: https://docs.djangoproject.com/en/3.2/ref/models/fields/#database-representation
    """
    category_A = models.ForeignKey(
        Category_A,
        on_delete = models.CASCADE
        )        
    name = models.CharField(
        max_length=200,
        )
    slug = models.SlugField(
        max_length=200, 
        unique=True           
        )

    class Meta:
        ordering = ("name",)
        verbose_name = 'catgory_B'
        verbose_name_plural = 'categories_B'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            'shop:product_list_by_category', 
            args=[self.slug],
            )
      
class Product(models.Model):
    # id = models.AutoField(primary_key=True) was added by default, not required explicitly
    category_B = models.ForeignKey(
        Category_B,
        related_name = 'products',
        on_delete = models.CASCADE
        )
    
    name = models.CharField(
        max_length = 100,
        )
    slug = models.SlugField(
        max_length = 100,
        )
    image = models.ImageField(
        upload_to = 'media/product_picture/%Y/%m/%d',
        blank = True
        )
    description = models.TextField(
        blank = True
        )
    price = models.DecimalField(
        max_digits = 5 ,
        decimal_places = 2
        )
        # ex.12345.12
    stock = models.PositiveIntegerField()
   
    available = models.BooleanField(
        default = True
        )
    created_at = models.DateTimeField(
        default = timezone.now
        )
        # Django3.2 Time zones : https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/#time-zones
    updated_at = models.DateTimeField(
        auto_now = True
        )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
