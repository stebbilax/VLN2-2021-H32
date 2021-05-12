from django.dispatch import receiver
from django.db.models.signals import post_save

from cart.models import Cart
from account.models import Account


@receiver(post_save, sender=Account)
def create_cart(sender, instance, created, **kwargs):
    """ Creates a cart for every Account created """
    if created:
        Cart.objects.create(account=instance)
