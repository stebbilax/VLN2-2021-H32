from django.db import models
from django.contrib.auth.models import User

from user.models import Product


class Cart(models.Model):
    """
    Cart Model is a layer of abstraction between the user and his select items
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    """
    CartItem Model links one product to one cart, keeping track of the quantity
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
