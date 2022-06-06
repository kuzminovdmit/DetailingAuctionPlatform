from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from accounts.views import car, create_car, index, LogoutView, PasswordChangeView


urlpatterns = [
    path('', index, name='index'),
    path('create-car', create_car, name='create_car'),
    path('my-car', car, name='car'),
    path('password_change', PasswordChangeView.as_view(), name='password_change'),
    path('logout', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('__debug__/', include('debug_toolbar.urls')),
    ]
