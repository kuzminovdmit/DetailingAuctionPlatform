from django.contrib import admin
from .models import Auction, Car, Order, Service


admin.site.register(Auction)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Service)
