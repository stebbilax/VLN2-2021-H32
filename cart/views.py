from django.shortcuts import render, HttpResponse
from .models import Cart, CartItem


# Create your views here.
def cart_page(request):
    cart = Cart.objects.filter(user=request.user)[0]
    items = CartItem.objects.filter(cart=cart)
    print(items)
    context = {'items': items}
    return render(request, 'cart/cart_page.html', context)