from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Account Model

    Attributes:
         user       - One to one relationship with the user model
         first_name - String field
         last_name  - String field
         photo      - Url to the account photo
     """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PaymentInfo(models.Model):
    """
    Payment Info Model

    Attributes:
        account             - One to one relationship with the Account model
        cvc                 - Integer field
        expiration_date     - Date field
        street_name         - String field
        house_number        - Integer field
        city                - String field
        postal_code         - String field
        name_of_cardholder  - String field
        card_number         - String field
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
    Search History Entry Model

    - Represents individual searches made by the user

    Attributes:
        account - One to one relationship with the Account model
        url     - String field
    """
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.url
        

