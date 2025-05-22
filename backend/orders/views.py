from django.shortcuts import redirect
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



