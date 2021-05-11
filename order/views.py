
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import PaymentInfoForm
from .decorators import make_order
from account.models import Account, PaymentInfo


@make_order
def index(request):
    try:
        account = get_object_or_404(Account, user=request.user)

    # If not get or create an account with the users device uuid
    except TypeError:
        device = request.COOKIES['device']
        account, created = Account.objects.get_or_create(device=device)

    if hasattr(account, 'paymentinfo'):
        info = PaymentInfo.objects.filter(account=account)[0]
        initial_info_obj = {
            'name': info.name_of_cardholder,
            'street_name': info.street_name,
            'house_number': info.house_number,
            'city': info.city,
            'postal_code': info.postal_code,
            'name_of_cardholder': info.name_of_cardholder,
            'card_number': info.card_number,
            'expiration_year': info.expiration_date.year,
            'expiration_month': info.expiration_date.month,
            'cvc': info.cvc
        }
        payment_form = PaymentInfoForm(initial=initial_info_obj)
    else:
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

