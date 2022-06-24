from django.urls import path

from accounts.views import DashboardView

from .views import AuctionCRUDView, AuctionCreateView, AuctionListView


app_name = 'auctions'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('auctions/', AuctionCRUDView.as_view(), name='auctions'),
    path('auctions/list', AuctionListView.as_view(), name='auction_list'),
    path('auctions/create', AuctionCreateView.as_view(), name='auction_create'),
]
