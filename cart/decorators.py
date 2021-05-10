from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from .models import CartItem, Cart, Account
from user.models import Product, ProductPhoto
from user.filters import GetPhotoFilter


def check_item_owner(view_func):
    """ Prevents a user from modifying another users cart items """

    def wrapper(request, *args, **kwargs):
        item_id = args[0]
        item = CartItem.objects.get(id=item_id)
        if item.cart.account.user != request.user:
            return HttpResponseBadRequest()

        return view_func(request, *args, **kwargs)

    return wrapper


# Todo handle exception
def collect_cart_info(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            account = get_object_or_404(Account, user=request.user)

        except TypeError:
            device = request.COOKIES['device']
            account, created = Account.objects.get_or_create(device=device)

        cart = Cart.objects.filter(account=account)[0]
        products = []
        summary_data = {'total': 0, 'number_of_items': 0}

        cart_items = cart.cartitem_set.all()
        for item in cart_items:
            products.append({"name": item.product.name,
                             "price": item.product.price,
                             "quantity": item.quantity,
                             "total": item.product.price * item.quantity,
                             "product_id": item.product.id,
                             "img": ProductPhoto.objects.filter(product=item.product)[0].photo.url})
            summary_data['total'] += item.product.price * item.quantity
            summary_data['number_of_items'] += 1

        return view_func(request, products, summary_data, *args, **kwargs)

    return wrapper
