from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import Menu

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product_data = item_data.pop("product")
            product, _ = Menu.objects.get_or_create(**product_data)
            OrderItem.objects.create(order=order, product=product, **item_data)
        return order