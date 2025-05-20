from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, OrderItem
from menu.models import Menu
from .serializers import OrderSerializer

class CreateOrderView(APIView):
    def post(self, request):
        customer_name = request.data.get('customer_name')
        products = request.data.get('products')

        if not customer_name or not products:
            return Response({"error": "Customer name and products are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the order
        order = Order.objects.create(customer_name=customer_name)

        for item in products:
            try:
                product = Menu.objects.get(id=item["product_id"])
                OrderItem.objects.create(order=order, product=product, quantity=item["quantity"])
            except Menu.DoesNotExist:
                return Response({"error": f"Product with ID {item['product_id']} not found."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Order created successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)

# Create your views here.

class OrderList(generics.ListCreateAPIView):
    """
    List all orders.
    """
    queryset = Order.objects.all().order_by('created_at')
    serializer_class = OrderSerializer

