from django.shortcuts import get_object_or_404
from datetime import datetime

from .forms import PaymentInfoForm
from order.models import Order, OrderContains
from account.models import PaymentInfo, Account

def make_order(view_func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            form = PaymentInfoForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                try:
                    account = get_object_or_404(Account, user=request.user)

                except TypeError:
                    device = request.COOKIES['device']
                    account, created = Account.objects.get_or_create(device=device)

                cart_items = account.cart.cartitem_set.all()
                total_price = 0
                for item in cart_items:
                    total_price += item.product.price
                order = Order.objects.create(
                    user=request.user,
                    total_price=total_price,
                    street_name=data['street_name'],
                    house_number=data['house_number'],
                    city=data['city'],
                    postal_code=data['postal_code']
                )
                for item in cart_items:
                    order_contains = OrderContains.objects.create(
                        order=order,
                        product=item.product,
                        quantity=item.quantity
                    )
                    order_contains.save()

                if data['save_info']:
                    expiration_year = data['expiration_year']
                    expiration_month = data['expiration_month']

                    PaymentInfo.objects.create(
                        account=account,
                        cvc=data['cvc'],
                        expiration_date= datetime(int(expiration_year), int(expiration_month), 1),
                        street_name=data['street_name'],
                        house_number=data['house_number'],
                        city=data['city'],
                        postal_code=data['postal_code'],
                        name_of_cardholder=data['name_of_cardholder'],
                        card_number=data['card_number']
                    )


            else:
                # Add messages here
                print('not valid')
                print(form.errors)

        return view_func(request, *args, **kwargs)
    return wrapper