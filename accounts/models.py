from enum import auto
from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auto = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    release_year = models.CharField(max_length=4)
    model = models.CharField(max_length=128)
    service = models.CharField(max_length=128, blank=True)
    
    def __str__(self) -> str:
        return self.user.username
