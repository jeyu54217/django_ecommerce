from django.db import models
from django.utils import timezone
from django.conf import settings # from demo_core import settings


# make_thumbnail
from io import BytesIO
from PIL import Image
from django.core.files import File
 

# class Category_A(models.Model):
#     name = models.CharField(
#         max_length=200,
#         )
#     slug = models.SlugField(
#         max_length=200, 
#         unique=True           
#         )
    
#     class Meta:
#         ordering = ("name",)
#         verbose_name = 'catgory_A'
#         verbose_name_plural = 'categories_A'
#         # why use verbose_name option? - To deal with the "s": https://1drv.ms/u/s!ArgTHAPiuIGQgcpJuzR5aAAhM6DNvg
   
#     def __str__(self): 
#         return self.name
#     def get_absolute_url(self):  
#         return f'/{self.slug}/'


# class Category_B(models.Model):
#     category_A = models.ForeignKey(
#         Category_A,
#         related_name = 'categories_B',
#         on_delete = models.CASCADE
#         )        
#     name = models.CharField(
#         max_length=200,
#         )
#     slug = models.SlugField(
#         max_length=200, 
#         unique=True           
#         )

#     class Meta:
#         ordering = ("name",)
#         verbose_name = 'catgory_B'
#         verbose_name_plural = 'categories_B'

#     def __str__(self): 
#         return self.name
#     def get_absolute_url(self):
#         return f'/{self.category_A.slug}/{self.slug}/'

# class Product(models.Model):
#     # id = models.AutoField(primary_key=True) was added by default, not required explicitly
#     category_B = models.ForeignKey(
#         Category_B,
#         related_name = 'products',
#         on_delete = models.CASCADE
#         )
#     name = models.CharField(
#         max_length = 100,
#         )
#     slug = models.SlugField()
#     description = models.TextField(
#         blank = True,
#         null = True,
#         )
#     price = models.DecimalField(
#         # ex.12345.12
#         max_digits = 5 ,
#         decimal_places = 2
#         )
#     stock = models.PositiveIntegerField()
#     image = models.ImageField(
#         upload_to = 'media/product_picture/%Y/%m/%d',
#         blank = True
#         )
#     thumbnail = models.ImageField(
#         upload_to = 'media/product_picture/%Y/%m/%d', 
#         blank = True, 
#         null = True
#         )
#     created_at = models.DateTimeField(
#         default = timezone.now
#         )
#     updated_at = models.DateTimeField(
#         auto_now = True
#         )

#     class Meta:
#         ordering = ("name",)

#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return f'/{self.category_B.slug}/{self.slug}/'
    
#     def get_image(self):
#         if self.image:
#             return settings.ROOT_URL+ self.image.url
#         return ''
    
#     def make_thumbnail(self, image, size=(300, 200)):
#         img = Image.open(image)
#         img.convert('RGB')
#         img.thumbnail(size)
        
#         _io = BytesIO()
#         img.save(_io, 'JPEG', quality=85)
        
#         thumbnail = File(_io, name = image.name)
#         return thumbnail
    
#     def get_thumbnail(self):
#         if self.thumbnail:
#             return settings.ROOT_URL + self.thumbnail.url
#         else:
#             if self.image:
#                 self.thumbnail = self.make_thumbnail(self.image)
#                 self.save()
#                 return settings.ROOT_URL + self.thumbnail.url
#             else:
#                 return ''
    

    
    
"""
    The hidden PK(id) field:
        1.The real database table for Category_B model will have a "category_A_id" column. 
        2.check : migrations/00xx_initial.py
        .See also: https://docs.djangoproject.com/en/3.2/ref/models/fields/#database-representation
    blank v.s. null
        https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
    related_name 
        https://stackoverflow.com/questions/44160983/what-does-related-name-do
    on_delete 
        https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    
"""
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

