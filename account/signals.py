from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from account.models import Account


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    """
    Creates an account for every user that is registered
    """
    if created:
        Account.objects.create(user=instance, email=instance.email)
