from django.db import models
from django.contrib.auth.models import User

from user.models import Product


class Order(models.Model):
    """
    Order model represents a single order made by user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    total_price = models.FloatField()
    street_name = models.CharField(max_length=300)
    house_number = models.IntegerField()
    city = models.CharField(max_length=300)
    postal_code = models.IntegerField()

    def __str__(self):
        return f"Order with ID: {self.id}"


class OrderContains(models.Model):
    """
    OrderContains model represents a single products appearance in an order
    and its quantity
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order Nr {self.order.id} contains {self.product}"