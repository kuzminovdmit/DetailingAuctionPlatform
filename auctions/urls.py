from django.urls import path

from auctions.views import AuctionCreateView, AuctionListView, OrderListView


app_name = 'auctions'

urlpatterns = [
    path(
        route='auction_create',
        view=AuctionCreateView.as_view(),
        name='auction_create'
    ),
    path(
        route='auction_list',
        view=AuctionListView.as_view(),
        name='auction_list'
    ),
    path(
        route='order_list/<str:status>',
        view=OrderListView.as_view(),
        name='order_list'
    ),
]