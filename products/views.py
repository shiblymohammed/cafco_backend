# products/views.py
from rest_framework import viewsets
from .models import Category, Product, OfferCategory
from .serializers import CategorySerializer, ProductSerializer, OfferCategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing categories.
    Provides `list` and `retrieve` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing products.
    Provides `list` and `retrieve` actions.
    """
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

class OfferCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing offers.
    Provides `list` and `retrieve` actions.
    """
    queryset = OfferCategory.objects.filter(is_active=True)
    serializer_class = OfferCategorySerializer