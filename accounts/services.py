from .models import Auction


def end_auction(auction_id):
    auction = Auction.objects.get(pk=auction_id)
    # TODO: create Order object
    auction.is_company_chosen = True
    auction.save()
