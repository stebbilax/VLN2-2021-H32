import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Cart, CartItem
from .decorators import check_item_owner, collect_cart_info

from account.models import Account


@collect_cart_info
def cart_page(request, products, summary_data):
    context = {'items': products, 'summary': summary_data}
    return render(request, 'cart/cart_page.html', context)


@collect_cart_info
def get_summary_info(request, products, summary_data):
    return JsonResponse({'summary': summary_data})


@check_item_owner
def increase_quantity(request, item_id):
    """
    Receives the id of a cart item and increments its value by one

    :param request:
    :param item_id:
    :return: HttpResponse
    """
    if request.method == 'POST':
        item = CartItem.objects.get(id=item_id)
        if item:
            item.quantity = item.quantity + 1
            item.save()
            return HttpResponse({item.quantity})
        else:
            return HttpResponseBadRequest()


@check_item_owner
def decrease_quantity(request, item_id):
    """
    Receives the id of a cart item and decrements its value by one

    :param request:
    :param item_id:
    :return: HttpResponse
    """
    if request.method == 'POST':
        item = CartItem.objects.get(id=item_id)
        if item:
            if item.quantity == 1:
                item.delete()
                return HttpResponse({0})
            else:
                item.quantity = item.quantity - 1
                item.save()
                return HttpResponse({item.quantity})
        else:
            return HttpResponseBadRequest()


def get_item_count(request):
    try:
        cart = request.user.account.cart
    except AttributeError:
        device = request.COOKIES['device']
        account, created = Account.objects.get_or_create(device=device)
        cart = account.cart

    return JsonResponse({'data': cart.cartitem_set.all().count()})


def remove_item(request, item_id):
    item = CartItem.objects.get(id=item_id)

    try:
        account = get_object_or_404(Account, user=request.user)

    except TypeError:
        device = request.COOKIES['device']
        account, created = Account.objects.get_or_create(device=device)

    if item:
        if item.cart.account == account:
            item.delete()
    return redirect("cart")
