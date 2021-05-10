from .forms import PaymentInfoForm
from order.models import Order
from account.models import PaymentInfo

def make_order(view_func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            form = PaymentInfoForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
            else:
                # Add messages here
                print('not valid')
                print(form.errors)

        return view_func(request, *args, **kwargs)
    return wrapper