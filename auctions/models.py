from django.db import models

from accounts.models import Car, Company


class Service(models.Model):
    CATEGORY_CHOICES = (
        (1, "Repair"),
        (2, "Maintenance"),
    )
    name = models.CharField(max_length=128)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'Service №{self.pk}'


class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_cost = models.PositiveSmallIntegerField()
    datetime_start = models.DateTimeField(auto_now_add=True)
    datetime_end = models.DateTimeField()
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return f'Auction №{self.pk}'


class Offer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    cost = models.PositiveSmallIntegerField()
    order_datetime_end = models.DateTimeField()

    class Meta:
        unique_together = ['company', 'auction']

    def __str__(self):
        return f'Offer №{self.pk}'


class Order(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    datetime_start = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Order №{self.pk}'