from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import WorkerManager


class Worker(AbstractUser):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)
    username = None

    objects = WorkerManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(
        Worker, on_delete=models.PROTECT, related_name="shops"
    )

    def __str__(self):
        return self.name


class Visit(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
