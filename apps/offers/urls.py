from django.urls import path

from .views import OfferCreateView


app_name = 'offers'

urlpatterns = [
    path('create/for-auction=<int:auction_pk>', OfferCreateView.as_view(), name='offer_create'),
]
