from django.urls import path

from .views import AuctionCreateView, AuctionDetailView, AuctionListView, AuctionUpdateView, delete_auction


app_name = 'auctions'

urlpatterns = [
    path('list', AuctionListView.as_view(), name='auction_list'),
    path('create', AuctionCreateView.as_view(), name='auction_create'),
    path('<int:pk>', AuctionDetailView.as_view(), name='auction_detail'),
    path('<int:pk>/update', AuctionUpdateView.as_view(), name='auction_update'),
    path('<int:pk>/delete/<int:from_detail>', delete_auction, name='auction_delete'),
]
