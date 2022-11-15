from rest_framework import serializers
# from .models import Category_A, Category_B, Product
from .models import  Category, Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            
            "get_image",
            "get_thumbnail",
            "get_absolute_url",
        )



class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True) # ListSerializer

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "products",
            
            "get_absolute_url",
        )


# class CategorySerializer_A(serializers.ModelSerializer):
#     category_B = CategorySerializer_B(many=True) # ListSerializer

#     class Meta:
#         model = Category
#         fields = (
#             "id",
#             "name",
#             "category_B",
            
#             "get_absolute_url",
#         )