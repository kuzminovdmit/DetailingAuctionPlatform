from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import Client, Representative, Car, Company
from auctions.models import Auction, Offer


class MainView(LoginRequiredMixin, TemplateView):
    redirect_field_name = ''
    template_name = 'dashboard/main.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

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
            client = Client.objects.get(user=user)
            cars = Car.objects.filter(client=client)
            
            context.update({
                'user_type': 'client',
                'client': client,
                'cars': cars,
                'auctions_in_progress': Auction.objects.filter(car__in=cars, is_ended=False),
                'auctions_closed': Auction.objects.filter(car__in=cars, is_ended=True),
            })

        if user.is_representative:
            representative = Representative.objects.get(user=user)
            company = Company.objects.get(representative=representative)

            context.update({
                'user_type': 'representative',
                'representative': representative,
                'company': company,
                'offers': Offer.objects.filter(company=company).select_related('auction'),
            })

        return context
