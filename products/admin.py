# products/admin.py
from django.contrib import admin
from .models import Category, SubCategory, Product, OfferCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(OfferCategory)
class OfferCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_percentage', 'is_active')
    filter_horizontal = ('products',)
    prepopulated_fields = {'slug': ('name',)}