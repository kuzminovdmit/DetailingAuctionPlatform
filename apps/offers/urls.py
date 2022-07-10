from django.urls import path

from .views import OfferCreateView, OfferListView


app_name = 'offers'

urlpatterns = [
    path('list', OfferListView.as_view(), name='offer_list'),
    path('create/for-auction=<int:auction_pk>', OfferCreateView.as_view(), name='offer_create'),
]
