from django.db import models

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
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity_available = models.IntegerField()
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.product_name

class CartItem(models.Model):

    username = models.CharField(max_length=30, blank=False, null=False)
    product_name = models.CharField(max_length=30, blank=False, null=False)
    category = models.CharField(max_length=30, blank=False, null=False)
    price = models.IntegerField()
    discount = models.IntegerField()
    quantity_added = models.IntegerField()

    def __str__(self):
        return (self.username, self.product_name)
