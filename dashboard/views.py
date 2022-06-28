from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import User, Client, Representative, Car, Company


class MainView(LoginRequiredMixin, TemplateView):
    redirect_field_name = ''
    template_name = 'dashboard/main.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_staff:
            return redirect(reverse('admin:index'))

        if not user.is_client and not user.is_representative:
            return redirect(reverse('accounts:choose_account'))

        return super(MainView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_client:
            context.update({
                'user_type': 'client',
                'client': Client.objects.get(user=user),
                'cars': Car.objects.filter(client__user=user)
            })
        elif user.is_representative:
            context.update({
                'user_type': 'representative',
                'representative': Representative.objects.get(user=user),
                'company': Company.objects.get(representative__user=user)
            })

        return context
