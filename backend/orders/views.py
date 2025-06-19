from django_asse import SseStreamView, JsonEvent
import asyncio
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderStream(SseStreamView):
    async def stream(self, request):
        while True:
            yield JsonEvent(event='order_update', data={'message': 'New Order update'})
            await asyncio.sleep(5)


