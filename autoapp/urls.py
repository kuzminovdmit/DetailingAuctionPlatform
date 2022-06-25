from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('auctions/', include('auctions.urls', namespace='auctions')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('__debug__/', include('debug_toolbar.urls')),
    ]
