from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetView
from django.urls import path, include

from accounts.views import DashboardView, AuctionCreateView, AuctionListView, SignInView, SignUpView


urlpatterns = [
    path(
        route='',
        view=DashboardView.as_view(),
        name='dashboard'
    ),
    path(
        route='auction_create',
        view=AuctionCreateView.as_view(),
        name='auction_create'
    ),
    path(
        route='auction_list',
        view=AuctionListView.as_view(),
        name='auction_list'
    ),
    path(
        route='sign-up',
        view=SignUpView.as_view(),
        name='sign_up'
    ),
    path(
        route='sign-in',
        view=SignInView.as_view(),
        name='sign_in'
    ),
    path(
        route='change-password',
        view=PasswordChangeView.as_view(
            template_name='password_change.html',
            success_url='/',
            extra_context={'password_change': True}
        ),
        name='password_change'
    ),
    # path(
    #     route='reset-password',
    #     view=PasswordResetView.as_view(
    #         template_name='password_reset.html',
    #         success_url='/',
    #         extra_context={'password_reset': True}
    #     ),
    #     name='password_reset'
    # ),
    path(
        route='logout',
        view=LogoutView.as_view(
            next_page='/',
        ),
        name='logout'
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('__debug__/', include('debug_toolbar.urls')),
    ]
