from django.urls import path, include
from .views import index, contact_us_page, about_us_page, products_page

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact_us_page, name='contact'),
    path('about', about_us_page, name='about'),
    path('products', products_page, name='products')
]
