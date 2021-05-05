import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, HttpResponse, redirect
from .models import Cart, CartItem



def cart_page(request):
    cart = Cart.objects.filter(user=request.user)
    if cart:
        cart = cart[0]
        items = CartItem.objects.filter(cart=cart)
        context = {'items': items}
    else:
        context = {'items': []}
    return render(request, 'cart/cart_page.html', context)


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
