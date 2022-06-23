from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from accounts.views import DashboardView


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('auctions/', include('auctions.urls', namespace='auctions')),
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('__debug__/', include('debug_toolbar.urls')),
    ]
