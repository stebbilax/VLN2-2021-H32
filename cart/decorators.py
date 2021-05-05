from django.http import HttpResponseBadRequest

from .models import CartItem


def check_item_owner(view_func):
    """ Prevents a user from modifying another users cart items """
    def wrapper(request, *args, **kwargs):
        item_id = args[0]
        item = CartItem.objects.get(id=item_id)
        if item.cart.user != request.user:
            return HttpResponseBadRequest()

        return view_func(request, *args, **kwargs)
    return wrapper
