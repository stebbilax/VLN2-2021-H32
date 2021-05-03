from django.shortcuts import render, HttpResponse


# Create your views here.
def order_page(request):
    return HttpResponse('Order page')