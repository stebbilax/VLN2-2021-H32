from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Account Model that represents the user profile if one is created
    Has a one-to-one relationship with the User Model
     """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, default='')
    last_name = models.CharField(max_length=300, default='')
    email = models.CharField(max_length=300, default='')
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'

    @property
    def photo_url(self):
        if self.photo:

            print(self.photo)
            return self.photo.url

        return 'https://t4.ftcdn.net/jpg/03/46/93/61/360_F_346936114_RaxE6OQogebgAWTalE1myseY1Hbb5qPM.jpg'


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
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.url
        

