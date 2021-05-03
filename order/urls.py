from django.urls import path, include
from .views import order_page

urlpatterns = [
    path('', order_page, name="order")
]