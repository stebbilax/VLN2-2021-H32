from django.urls import path, include
from .views import home_page, contact_us_page, about_us_page, products_page

urlpatterns = [
    path('', home_page, name='home'),
    path('contact', contact_us_page, name='contact'),
    path('about', about_us_page, name='about'),
    path('products', products_page, name='products')
]
