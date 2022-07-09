from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse

from .forms import AuctionCreationForm
from .models import Auction


class AuctionListView(ListView):
    model = Auction
    context_object_name = 'auctions'
    template_name = 'auctions/auction_list.html'

    def get_queryset(self):
        user = self.request.user

        if user.is_client:
            queryset = Auction.objects.filter(car__client__user=user).select_related('service')
        elif user.is_representative:
            queryset = Auction.objects.filter(
                is_ended=False, service__in=user.representative.company.services.all()).select_related('service')
        else:
            queryset = Auction.objects.all()

        return queryset


class AuctionCreateView(CreateView):
    model = Auction
    form_class = AuctionCreationForm
    template_name = 'auctions/auction_create.html'

    def get_form_kwargs(self):
        kwargs = super(AuctionCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class AuctionDetailView(DetailView):
    model = Auction
    queryset = Auction.objects.select_related('car', 'car__client__user', 'service')
    template_name = 'auctions/auction_detail.html'


class AuctionUpdateView(UpdateView):
    model = Auction
    form_class = AuctionCreationForm
    template_name = 'auctions/auction_update.html'

    def get_form_kwargs(self):
        kwargs = super(AuctionUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


@require_http_methods(['DELETE'])
def delete_auction(request, pk: int, from_detail: int):
    auction = get_object_or_404(Auction, pk=pk)
    auction.delete()

    if from_detail:
        response = HttpResponse()
        response["HX-Redirect"] = reverse('auctions:auction_list')
        return response

    return render(request, 'auctions/auctions_items.html', {
        'auctions': Auction.objects.select_related('car', 'car__client__user', 'service')})
