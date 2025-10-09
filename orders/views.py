# orders/views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for creating and viewing orders.
    For Day 1, this will allow creating new orders.
    Listing/retrieving will be locked down later.
    """
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

class MyOrderListView(generics.ListAPIView):
    """
    Returns a list of orders for the currently authenticated user.
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # We need to link the NextAuth user to our UserProfile.
        # For now, we'll match by email.
        user_email = self.request.user.email
        return Order.objects.filter(user_email=user_email).order_by('-created_at')