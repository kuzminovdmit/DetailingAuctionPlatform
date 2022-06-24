from django.views.generic import CreateView, ListView, TemplateView

from .forms import AuctionCreationForm
from .models import Auction, Order


class AuctionCRUDView(TemplateView):
    template_name = 'auctions/auctions.html'


class AuctionCreateView(CreateView):
    model = Auction
    form_class = AuctionCreationForm
    template_name = 'auctions/auction_create.html'

    def get_form_kwargs(self):
        kwargs = super(AuctionCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class AuctionListView(ListView):
    model = Auction
    context_object_name = 'auctions'
    template_name = 'auctions/auction_list.html.html'
    queryset = Auction.objects.filter(is_ended=True)


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order_list.html'

    def get_queryset(self):
        status = self.kwargs.get('status')
        is_completed = False

        if status == 'in_progress':
            is_completed = False
        elif status == 'completed':
            is_completed = True

        return super(OrderListView, self).get_queryset().filter(
            auction__car=self.request.user.car,
            is_completed=is_completed
        )

