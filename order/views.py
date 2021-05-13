from django.shortcuts import render, get_object_or_404, redirect

from .forms import PaymentInfoForm
from .decorators import make_order

from account.models import Account, PaymentInfo


@make_order
def checkout_page(request):
    """
    Handles GET requests to the order page.
    If user has at least one element in their cart, return info about that item
    If user has no items in their cart, redirect to the products page.
    """
    try:
        account = get_object_or_404(Account, user=request.user)

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

    cart = account.cart
    cart_items = cart.cartitem_set.all()

    # If cart is empty, redirect
    if len(cart_items) == 0:
        return redirect('products', 'cereal')

    cart_info = {'count': 0, 'price': 0}
    for item in cart_items:
        cart_info['count'] += 1 * item.quantity
        cart_info['price'] += item.product.price * item.quantity

    context = {'form': payment_form, 'cart_info': cart_info}
    return render(request, 'order/order.html', context)
