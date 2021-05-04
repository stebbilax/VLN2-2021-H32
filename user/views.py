from django.shortcuts import render, HttpResponse



# Create your views here.
def index(request):
    return render(request, 'cart/index.html')


def about_us_page(request):
    return HttpResponse('About us')


def contact_us_page(request):
    return HttpResponse('Contact us')


def products_page(request):
    return HttpResponse('Products')