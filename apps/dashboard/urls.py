from django.urls import path

from .views import MainView


app_name = 'dashboard'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
