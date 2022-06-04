from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal


class Car(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    release_year = models.CharField(max_length=4)
    model = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return f"Автомобиль клиента {self.client.username}"


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


class Service(models.Model):
    CATEGORY_CHOICES = (
        (1, "Ремонт"),
        (2, "Обслуживание"),
    )
    name = models.CharField(max_length=128)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    chosen_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    timer_start = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Аукцион по предоставлению услуги {self.chosen_service} для {self.car}, начавшийся в {self.timer_start}"

    def timer_end(self):
        return self.timer_start + timedelta(minutes=1)


auction_done = Signal()

@receiver(auction_done, sender=Auction)
def finish_auction(sender, instance, created, **kwargs):
    instance.is_finished = True
    instance.save()


class Order(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    cost = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Услуга {self.auction.chosen_service}, выполняемая {self.company} для {self.auction.car}"
