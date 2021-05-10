from django.urls import path, include
from .views import cart_page, increase_quantity, decrease_quantity, get_item_count, remove_item

urlpatterns = [
    path('', cart_page, name="cart"),
    path('get_item_count/', get_item_count, name='get_item_count'),
    path('increase_quantity/<int:item_id>', increase_quantity, name="increase_quantity"),
    path('decrease_quantity/<int:item_id>', decrease_quantity, name="decrease_quantity"),
    path('remove_item/<int:item_id>', remove_item, name="remove_item"),
]
