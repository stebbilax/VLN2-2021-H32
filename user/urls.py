from django.urls import path, include
from .views import (index, contact_us_page, about_us_page, products_page, get_product_data,
                    get_keywords, product_page)

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact_us_page, name='contact'),
    path('about/', about_us_page, name='about'),
    path('products/<str:category>/', products_page, name='products'),
    path('product/<int:id>/', product_page, name='product'),
    path('get_product_data/<str:category>/', get_product_data, name='get_product_data'),
    path('keywords/', get_keywords, name='get_keywords')
]
