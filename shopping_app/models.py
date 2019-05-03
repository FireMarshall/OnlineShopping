from django.db import models
from django.utils.timezone import now
import datetime
# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=25, blank=False, null=False)
    password = models.CharField(max_length=12, blank=False, null=False)
    mobile = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):

    product_name = models.CharField(max_length=30, blank=False, null=False)
    category = models.CharField(max_length=30, blank=False, null=False)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    quantity_available = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=datetime.datetime.now())
    img_link = models.URLField(default="www.google.com")

    def __str__(self):
        return self.product_name


class CartItem(models.Model):

    username = models.CharField(max_length=30, blank=False, null=False)
    product_name = models.CharField(max_length=30, blank=False, null=False)
    category = models.CharField(max_length=30, blank=False, null=False)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    quantity_added = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
