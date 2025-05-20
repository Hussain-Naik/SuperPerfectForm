from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import Menu

class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source='menu.name')

    class Meta:
        model = OrderItem
        fields = ['item', 'item_name', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        products_data = validated_data.pop('orderitem_set', [])
        order = Order.objects.create(**validated_data)

        for item_data in products_data:
            OrderItem.objects.create(order=order, **item_data)

        return order