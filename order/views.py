from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import PaymentInfoForm
from .decorators import make_order
from account.models import Account


@make_order
def index(request):
    payment_form = PaymentInfoForm()
    try:
        account = get_object_or_404(Account, user=request.user)

    except TypeError:
        device = request.COOKIES['device']
        account, created = Account.objects.get_or_create(device=device)

    cart = account.cart
    cart_items = cart.cartitem_set.all()
    cart_info = {'count': 0, 'price': 0}
    for item in cart_items:
        cart_info['count'] += 1
        cart_info['price'] += item.product.price

    context = {'form': payment_form, 'cart_info': cart_info }
    return render(request, 'order/order.html', context)


def place_order(request):
    return HttpResponse('place order')


def send_confirmation_email(request):
    return HttpResponse('send confirmation email')


def save_payment_info(request):
    return HttpResponse('save payment info')


def checkout(request):
    return HttpResponse('checkout')

