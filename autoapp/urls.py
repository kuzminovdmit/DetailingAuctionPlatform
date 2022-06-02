from django.contrib import admin
from django.urls import path

from accounts.views import account, create_account, index


urlpatterns = [
    path('', index, name='index'),
    path('create-account', create_account, name='create_account'),
    path('account', account, name='account'),
    path('admin/', admin.site.urls),
]
