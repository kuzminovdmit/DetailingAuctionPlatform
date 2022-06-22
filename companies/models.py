from django.db import models


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