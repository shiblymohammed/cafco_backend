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
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] # <--- ADD THIS BACK

    def get_queryset(self):
        # Now we can safely use request.user because JWTAuthentication populated it
        return Order.objects.filter(user_email=self.request.user.email).order_by('-created_at')