from django.db import models
from django.contrib.auth.models import User

from user.models import Product
from account.models import Account


class Cart(models.Model):
    """
    Cart Model is a layer of abstraction between the user and his select items
    """
    account = models.OneToOneField(Account, on_delete=models.CASCADE,
                                   null=True)

    def __str__(self):
        return f"{self.account.id}'s Cart"


class CartItem(models.Model):
    """
    CartItem Model links one product to one cart, keeping track of the quantity
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Cart: {self.cart}, Item: {self.product}"
