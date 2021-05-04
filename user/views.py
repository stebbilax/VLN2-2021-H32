from django.shortcuts import render, HttpResponse
from .models import Product


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def about_us_page(request):
    return HttpResponse('About us')


def contact_us_page(request):
    return HttpResponse('Contact us')


def products_page(request):
    """ Displays product page """
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'user/products.html', context)
