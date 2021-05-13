from django.db import models
from django.contrib.auth.models import User

from user.models import Product


class Account(models.Model):
    """
    Account Model that represents the user profile if one is created
    Has a one-to-one relationship with the User Model
     """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=300, default='')
    last_name = models.CharField(max_length=300, default='')
    email = models.CharField(max_length=300, default='')
    photo = models.ImageField(null=True, blank=True)
    device = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url

        return 'https://ship-o-cereal-bucket.s3.amazonaws.com/default_4ShsN9O.jpg?AWSAccessKeyId=AKIARUQJJGSAX4RFXTUO&Signature=SP2SaciykV7FUhwr9OMTu1GO9es%3D&Expires=1620332994'


class PaymentInfo(models.Model):
    """
    Payment Info Model stores various payment information
    Has a one-to-one relationship with the Account Model
    """
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    cvc = models.IntegerField()
    expiration_date = models.DateField()
    street_name = models.CharField(max_length=300)
    house_number = models.IntegerField()
    city = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=300)
    name_of_cardholder = models.CharField(max_length=400)
    card_number = models.CharField(max_length=300)

    def __str__(self):
        return self.card_number


class SearchHistoryEntry(models.Model):
    """
    Search History Entry Model Represents individual searches made by a user
    Has a many-to-one relationship with the Account Model
    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
        

