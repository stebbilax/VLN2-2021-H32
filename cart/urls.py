from django.urls import path, include
from .views import cart_page

urlpatterns = [
    path('', cart_page, name="cart")
]