from django.urls import path, include
from .views import cart_page, increase_quantity, decrease_quantity

urlpatterns = [
    path('', cart_page, name="cart"),
    path('increase_quantity/<int:item_id>', increase_quantity, name="increase_quantity"),
    path('decrease_quantity/<int:item_id>', decrease_quantity, name="decrease_quantity"),
]