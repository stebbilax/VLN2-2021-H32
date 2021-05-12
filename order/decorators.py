from django.shortcuts import get_object_or_404, render
from datetime import datetime

from .utils import create_order, create_payment_info, send_confirmation_email
from .forms import PaymentInfoForm
from account.models import Account


def make_order(view_func):
    """

    :param view_func:
    :return:
    """
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
                create_order(cart_items, request.user, data)

                if data['save_info']:
                    create_payment_info(account, data)

                send_confirmation_email(account)

                return render(request, 'order/checkout-confirmation.html')

            else:
                context = {'form': form}
                return render(request, 'order/order.html', context)

        return view_func(request, *args, **kwargs)

    return wrapper
