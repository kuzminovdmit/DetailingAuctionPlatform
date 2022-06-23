from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    release_year = models.CharField(max_length=4)
    model = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'Car №{self.pk}'


class Company(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return f'Company №{self.pk}'


class Representative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'company']

    def __str__(self):
        return f'Representative №{self.pk}'

