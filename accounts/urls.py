from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetView
from django.urls import path

from accounts.views import SignInView, SignUpView


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
        template_name='password_reset.html',
        success_url='/',
        extra_context={'password_reset': True}
    ), name='password_reset'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
]