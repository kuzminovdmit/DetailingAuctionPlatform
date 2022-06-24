from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy

from .forms import AuctionCreationForm
from .models import Auction, Order


class AuctionCRUDView(TemplateView):
    template_name = 'auctions/auctions.html'


class AuctionCreateView(CreateView):
    model = Auction
    form_class = AuctionCreationForm
    template_name = 'auctions/auction_create.html'
    success_url = reverse_lazy('auctions:auction_list')

    def get_form_kwargs(self):
        kwargs = super(AuctionCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class AuctionListView(ListView):
    model = Auction
    context_object_name = 'auctions'
    template_name = 'auctions/auction_list.html.html'
    queryset = Auction.objects.filter(is_ended=False)

