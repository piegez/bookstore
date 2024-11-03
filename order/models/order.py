from django.db import models
from django.contrib.auth.models import User

from product.models.product import Product


class Order(models.Model):
    objects = None
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
