from django.urls import path

from .views import AuctionCRUDView, AuctionCreateView, AuctionListView


app_name = 'auctions'

urlpatterns = [
    path('', AuctionCRUDView.as_view(), name='auctions'),
    path('list', AuctionListView.as_view(), name='auction_list'),
    path('create', AuctionCreateView.as_view(), name='auction_create'),
]
