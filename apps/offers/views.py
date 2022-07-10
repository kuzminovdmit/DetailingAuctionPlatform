from django.views.generic import CreateView, ListView

from apps.accounts.models import Company
from apps.auctions.models import Auction

from .forms import OfferCreationForm
from .models import Offer


class OfferListView(ListView):
    model = Offer
    template_name = 'offers/offer_list.html'
    context_object_name = 'offers'

    def get_queryset(self, *args, **kwargs):
        return Offer.objects.filter(company__representative__user=self.request.user)


class OfferCreateView(CreateView):
    model = Offer
    form_class = OfferCreationForm
    template_name = 'offers/offer_create.html'

    def get_context_data(self, **kwargs):
        context = super(OfferCreateView, self).get_context_data()
        context.update({
            'auction': Auction.objects.get(pk=self.kwargs['auction_pk']),
            'company': Company.objects.get(representative__user=self.request.user)
        })
        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        form.instance.auction = context['auction']
        form.instance.company = context['company']

        return super(OfferCreateView, self).form_valid(form)
