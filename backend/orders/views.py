from rest_framework import generics
from .models import Order, OrderItems
from .serializers import OrderSerializer

# Create your views here.

class OrderList(generics.ListCreateAPIView):
    """
    List all orders.
    """
    queryset = Order.objects.all().order_by('created_at')
    serializer_class = OrderSerializer

