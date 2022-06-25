from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Car(models.Model):
    client = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'company']

    def __str__(self):
        return f'Representative №{self.pk}'

