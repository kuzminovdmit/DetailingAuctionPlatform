from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetView, TemplateView
from django.urls import path

from .views import SignInView, SignUpView, CarDetailView, CarCreateView, CarListView, CompanyCreateView


app_name = 'accounts'

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name='sign_up'),
    path('sign-in', SignInView.as_view(), name='sign_in'),
    path('change-password', PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url='/',
        extra_context={'password_change': True}
    ), name='password_change'),
    path('reset-password', PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        success_url='/',
        extra_context={'password_reset': True}
    ), name='password_reset'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),

    path('choose-account', TemplateView.as_view(
        template_name='accounts/choose_account.html'), name='choose_account'),
    path('cars', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
    path('cars/create', CarCreateView.as_view(), name='car_create'),
    path('company/create', CompanyCreateView.as_view(), name='company_create'),
]
