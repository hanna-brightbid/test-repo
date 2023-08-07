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

class InventoryItemListEmbargoDateRange(generics.ListCreateAPIView):
    serializer_class = OrderTagSerializer

    def get_queryset(self):
        start_date_str = self.request.query_params.get('start_date')
        embargo_date_str = self.request.query_params.get('embargo_date')
        if embargo_date_str and start_date_str:
            try:
                embargo_date = timezone.datetime.strptime(embargo_date_str, '%Y-%m-%d')
                start_date = timezone.datetime.strptime(start_date_str, '%Y-%m-%d')
                return OrderTag.objects.filter(start_date=start_date, embargo_date=embargo_date))
            except ValueError:
                pass
        return OrderTag.objects.none()    