from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.model} - {self.manufacturer}"
