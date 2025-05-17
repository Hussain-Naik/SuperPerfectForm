from rest_framework import serializers
from .models import Order, OrderItems

class OrderSerializer(serializers.ModelSerializer):
    '''
    serializer for orders
    '''

    class Meta:
        model = Order
        fields = '__all__'