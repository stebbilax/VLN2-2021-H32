from django.urls import path, include
from .views import checkout_page


urlpatterns = [
    path('', checkout_page, name="order"),
]
