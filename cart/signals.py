from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cart.models import Cart
from account.models import Account


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        account = Account.objects.get(user=instance)
        Cart.objects.create(account=account)
