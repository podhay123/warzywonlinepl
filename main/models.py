from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ManyToManyField(Category)
    # seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Opinion(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )


class ProductToSell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(1)]
    )
    quantity = models.IntegerField(
        validators=[MaxValueValidator(999), MinValueValidator(1)]
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_products = models.ManyToManyField(
        ProductToSell, blank=True
    )  # to tak działa XD?


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# null=True blank=True????
