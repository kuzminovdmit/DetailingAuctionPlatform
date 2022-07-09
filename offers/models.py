from django.db import models


class Offer(models.Model):
    company = models.ForeignKey('accounts.Company', on_delete=models.CASCADE)
    auction = models.ForeignKey('auctions.Auction', on_delete=models.CASCADE)
    cost = models.PositiveSmallIntegerField()
    order_datetime_end = models.DateTimeField()
    is_chosen = models.BooleanField(default=False)

    class Meta:
        unique_together = ['company', 'auction']

    def __str__(self):
        return f'Offer №{self.pk}'
