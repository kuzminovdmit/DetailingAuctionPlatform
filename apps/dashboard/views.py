from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse

from apps.accounts.models import Client, Representative, Car, Company
from apps.auctions.models import Auction, Order
from apps.offers.models import Offer


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
                'orders': Order.objects.filter(offer__auction__car__in=cars)
            })

        if user.is_representative:
            representative = Representative.objects.get(user=user)
            company = Company.objects.get(representative=representative)
            offers = Offer.objects.filter(company=company).select_related('auction')

            context.update({
                'user_type': 'representative',
                'representative': representative,
                'company': company,
                'offers': offers,
                'orders': Order.objects.filter(offer__in=offers)
            })

        return context
