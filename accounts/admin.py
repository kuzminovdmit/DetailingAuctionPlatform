from django.contrib import admin
from .models import Auction, Car, Company, Order, Service


admin.site.register(Auction)
admin.site.register(Car)
admin.site.register(Company)
admin.site.register(Order)
admin.site.register(Service)
