from rest_framework import serializers
from .models import Order, OrderItem, Product
# from menu.models import Menu

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "price"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'reference', 'customer', 'paid', 'completed', 'items', 'total']

    def get_total(self, obj):
        return sum(item.price * item.quantity for item in obj.orderitem_set.all())

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product_data = item_data.pop("product")
            product, _ = Product.objects.get_or_create(**product_data)
            item_data["price"] = product.price
            OrderItem.objects.create(order=order, product=product, **item_data)
        return order

class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'reference', 'customer', 'paid', 'completed', 'items']