from django.contrib.auth.views import TemplateView, PasswordChangeView, LogoutView
from django.urls import path, reverse_lazy

from .views import (
    SignInView, SignUpView,
    CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView,
    CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView
)


app_name = 'accounts'

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name='sign_up'),
    path('sign-in', SignInView.as_view(), name='sign_in'),
    path('choose-account', TemplateView.as_view(
        template_name='accounts/choose_account.html'),
        name='choose_account'
    ),
    path('change-password', PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url=reverse_lazy('dashboard:main'),
        extra_context={'password_change': True}
    ), name='password_change'),
    path('logout', LogoutView.as_view(
        next_page='/'
    ), name='logout'),

    path('cars', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('cars/create', CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/edit', CarUpdateView.as_view(), name='car_edit'),
    path('cars/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),

    path('companies', CompanyListView.as_view(), name='company_list'),
    path('companies/<int:pk>', CompanyDetailView.as_view(), name='company_detail'),
    path('companies/create', CompanyCreateView.as_view(), name='company_create'),
    path('companies/<int:pk>/edit', CompanyUpdateView.as_view(), name='company_edit'),
    path('companies/<int:pk>/delete', CompanyDeleteView.as_view(), name='company_delete'),
]
