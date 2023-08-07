
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, InventoryItemListAfterDate


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('tags/after_date/', InventoryItemListAfterDate.as_view(), name='order-detail_after_date'),

]