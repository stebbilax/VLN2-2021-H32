from django.shortcuts import get_object_or_404

from .forms import PaymentInfoForm
from order.models import Order, OrderContains
from account.models import PaymentInfo, Account

def make_order(view_func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            form = PaymentInfoForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                try:
                    account = get_object_or_404(Account, user=request.user)

                except TypeError:
                    device = request.COOKIES['device']
                    account, created = Account.objects.get_or_create(device=device)

                cart_items = account.cart.cartitem_set.all()
                order = Order.objects.create(
                    user=request.user,
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
                    order.total_price += item.product.price * item.quantity
                    order_contains.save()

                order.save()

                if data['save_info']:
                    pass
                    # PaymentInfo.objects.create(
                    #     account=account,
                    #     cvc=data['cvc'],
                    #     expiration_date=''
                    # )


            else:
                # Add messages here
                print('not valid')
                print(form.errors)

        return view_func(request, *args, **kwargs)
    return wrapper