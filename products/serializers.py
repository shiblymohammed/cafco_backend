# products/serializers.py
from rest_framework import serializers
from .models import Category, SubCategory, Product, OfferCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    active_offer = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'category', 
            'subcategory', 'material', 'color', 'dimensions', 
            'price', 'image_url', 'is_active', 'active_offer'
        ]
    
    def get_active_offer(self, obj):
        # Find the first active offer for this product
        active_offer = obj.offers.filter(is_active=True).first()
        if active_offer:
            return active_offer.discount_percentage
        return None
        

class OfferCategorySerializer(serializers.ModelSerializer):
    # Explicitly use the ProductSerializer for the nested products
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = OfferCategory
        fields = ['id', 'name', 'slug', 'discount_percentage', 'is_active','image_url', 'products']