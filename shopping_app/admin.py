from django.contrib import admin
from shopping_app.models import User, Product, CartItem

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(CartItem)