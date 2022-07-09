from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.dashboard.urls', namespace='dashboard')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('auctions/', include('apps.auctions.urls', namespace='auctions')),
    path('offers/', include('apps.offers.urls', namespace='offers')),
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('__debug__/', include('debug_toolbar.urls')),
    ]
