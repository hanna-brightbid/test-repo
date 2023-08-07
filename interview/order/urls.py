
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView,InventoryItemListStartDateEmbargoDate


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('tags/start_embargo_date/', InventoryItemListStartDateEmbargoDate.as_view(), name='order-detail_start_embargo_date'),
]