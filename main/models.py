from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ManyToManyField(Category)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Opinion(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )

    def __str__(self) -> str:
        return "user: " + self.name + "\n" + "description: " + self.description
