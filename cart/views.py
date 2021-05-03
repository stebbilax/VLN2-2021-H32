from django.shortcuts import render, HttpResponse


# Create your views here.
def cart_page(request):
    return HttpResponse('Cart page')