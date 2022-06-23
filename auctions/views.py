from django.views.generic import CreateView, ListView

from .forms import AuctionCreationForm
from .models import Auction, Order


class AuctionCreateView(CreateView):
    template_name = 'car_service.html'
    form_class = AuctionCreationForm
    success_url = 'auction_list'

    def form_valid(self, form):
        form.instance.car = self.request.user.car
        return super(AuctionCreateView, self).form_valid(form)


class AuctionListView(ListView):
    model = Auction
    context_object_name = 'auctions'
    template_name = 'auction_list.html'
    queryset = Auction.objects.filter(is_ended=False)


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

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data()
        context['is_completed'] = self.kwargs.get('is_completed', False)
        return context
