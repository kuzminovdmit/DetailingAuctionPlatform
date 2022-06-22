from companies.models import Company
from .models import Auction, Order


def end_auction(auction_id):
    auction = Auction.objects.get(pk=auction_id)
    order = Order.objects.create(
        auction=auction,
        company=Company.objects.first()
    )
    order.save()
    auction.is_company_chosen = True
    auction.save()
