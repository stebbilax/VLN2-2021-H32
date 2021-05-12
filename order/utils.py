from datetime import datetime

from django.core.mail import send_mail
from django.contrib.auth.models import User

from order.models import Order, OrderContains
from account.models import PaymentInfo


def create_order(cart_items, user, data):
    """
    Creates an Order and OrderContains objects for every product in the users cart
    Clears cart of any items in the order.
    """
    total_price = 0
    for item in cart_items:
        total_price += item.product.price
    try:
        order = Order.objects.create(
            user=user,
            total_price=total_price,
            street_name=data['street_name'],
            house_number=data['house_number'],
            city=data['city'],
            postal_code=data['postal_code']
        )
    # If the user is anonymous, make a new user unique to this order
    except ValueError:
        username = "anonymous-"+str(hash(f"{total_price}{data['street_name']}{datetime.now()}"))
        password = hash(f"{data['house_number']}{data['city']}{datetime.now()}")

        anon_user = User(username=username, password=password)
        anon_user.save()
        order = Order.objects.create(
            user=anon_user,
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
        item.delete()


def create_payment_info(account, data):
    """
    Creates a PaymentInfo object belonging to the user.
    If any such object already exists it is overwritten
    """
    expiration_year = data['expiration_year']
    expiration_month = data['expiration_month']

    # Check if payment info already exists and delete if it does
    try:
        old_info = PaymentInfo.objects.get(account=account).delete()
    except PaymentInfo.DoesNotExist:
        pass

    PaymentInfo.objects.create(
        account=account,
        cvc=data['cvc'],
        expiration_date=datetime(int(expiration_year), int(expiration_month), 1),
        street_name=data['street_name'],
        house_number=data['house_number'],
        city=data['city'],
        postal_code=data['postal_code'],
        name_of_cardholder=data['name_of_cardholder'],
        card_number=data['card_number']
    )


def send_confirmation_email(account):
    """
    Sends an order confirmation to the email belonging to the account
    """
    if account.email:
        send_mail(
            'Ship o Cereal!',
            'Your order is on its way.',
            'from@example.com',
            [account.email],
            fail_silently=False,
        )
