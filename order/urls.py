from django.urls import path, include
from .views import index, place_order, send_confirmation_email, save_payment_info, checkout


urlpatterns = [
    path('', index, name="order"),
    path('placeorder/', place_order),
    path('sendconfirmationemail/', send_confirmation_email),
    path('savepaymentinfo/', save_payment_info),
    path('checkout/', checkout)
]
