from django.contrib import admin
from django.urls import path, include

from accounts.views import car, create_car, index


urlpatterns = [
    path('', index, name='index'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('create-account', create_car, name='create_car'),
    path('account', car, name='car'),
    path('admin/', admin.site.urls),
]
