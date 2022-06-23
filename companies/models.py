from django.db import models

from accounts.models import Auction


class Company(models.Model):
    CITY_CHOICES = (
        ('MSK', 'Москва'),
        ('SPB', 'Санкт-Петербург'),
        ("YAR", "Ярославль"),
    )
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=3, choices=CITY_CHOICES, default='MSK')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'


class Offer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    cost = models.PositiveSmallIntegerField()
    order_datetime_end = models.DateTimeField()

    def __str__(self):
        return f'Offer №{self.pk}'
