from django.contrib import admin

from .models import Service, Auction, Offer, Order


admin.site.register(Service)
admin.site.register(Auction)
admin.site.register(Offer)
admin.site.register(Order)