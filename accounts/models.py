from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django_q.models import Schedule


class Car(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    release_year = models.CharField(max_length=4)
    model = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'Автомобиль №{self.id}'


class Service(models.Model):
    CATEGORY_CHOICES = (
        (1, "Ремонт"),
        (2, "Обслуживание"),
    )
    name = models.CharField(max_length=128)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


def get_default_timer_end():
    return timezone.now() + timedelta(seconds=10)


class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    chosen_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    task_id = models.IntegerField(default=0)
    datetime_start = models.DateTimeField(auto_now_add=True)
    datetime_end = models.DateTimeField(default=get_default_timer_end)
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return f'Аукцион №{self.id}'

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Auction, self).save(*args, **kwargs)

        # if not self.task_id:
        #     task = Schedule.objects.create(
        #         name=self.__str__(),
        #         func='accounts.services.end_auction',
        #         kwargs={'auction_id': self.pk},
        #         schedule_type=Schedule.ONCE,
        #         next_run=self.datetime_end
        #     )
        #     self.task_id = task.pk

        super(Auction, self).save(*args, **kwargs)


class Order(models.Model):
    offer = models.ForeignKey('companies.Offer', on_delete=models.CASCADE)
    datetime_start = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Заказ №{self.id}'
