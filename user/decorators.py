from django.shortcuts import get_object_or_404

from .models import Product
from account.models import SearchHistoryEntry, Account


def record_search_history(view_func):
    """
    Creates a search history object if there is an account
    associated with the request user. If the product does not
    exist, raise a 404.
    """

    def wrapper(request, id, *args, **kwargs):
        product = get_object_or_404(Product, pk=id)
        try:
            account = Account.objects.get(user=request.user)
            SearchHistoryEntry.objects.create(account=account, product=product)

        except TypeError:
            pass

        return view_func(request, product, *args, **kwargs)

    return wrapper
