from django.shortcuts import render
from rest_framework import generics
from django.utils import timezone

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class InventoryItemListAfterDate(generics.ListCreateAPIView):
    serializer_class = OrderTagSerializer

    def get_queryset(self):
        start_date_str = self.request.query_params.get('start_date')
        if start_date_str:
            try:
                start_date = timezone.datetime.strptime(start_date_str, '%Y-%m-%d')
                return OrderTag.objects.filter(start_date__gt=start_date)
            except ValueError:
                pass
        return OrderTag.objects.none()    