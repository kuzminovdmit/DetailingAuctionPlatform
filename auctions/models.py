from datetime import timedelta
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
    FAST = 10
    NORMAL = 60
    SLOW = 1440
    DURATION_CHOICES = (
        (FAST, '10 minutes'),
        (NORMAL, '1 hour'),
        (SLOW, '1 day'),
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_cost = models.PositiveSmallIntegerField()
    datetime_start = models.DateTimeField(auto_now_add=True)
    duration_choice = models.PositiveSmallIntegerField(choices=DURATION_CHOICES, default=FAST)
    datetime_end = models.DateTimeField(blank=True, null=True)
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return f'Auction №{self.pk}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            super(Auction, self).save(*args, **kwargs)

        if not self.datetime_end:
            self.datetime_end = self.datetime_start + timedelta(minutes=self.duration_choice)

        super(Auction, self).save(*args, **kwargs)


class Offer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    cost = models.PositiveSmallIntegerField()
    order_datetime_end = models.DateTimeField()
    is_chosen = models.BooleanField(default=False)

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