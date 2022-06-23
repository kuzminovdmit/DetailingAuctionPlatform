from django.db import models

from accounts.models import Auction


class Company(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return f'Company №{self.pk}'


class Offer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    cost = models.PositiveSmallIntegerField()
    order_datetime_end = models.DateTimeField()

    class Meta:
        unique_together = ['company', 'auction']

    def __str__(self):
        return f'Offer №{self.pk}'
