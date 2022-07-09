from django.contrib import admin

from .models import Service, Auction, Order


admin.site.register(Service)
admin.site.register(Auction)
admin.site.register(Order)
