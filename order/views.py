from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django import forms


# Create your views here.
def index(request):
    return render(request, 'order/index.html')


def place_order(request):
    return HttpResponse('place order')


def send_confirmation_email(request):
    return HttpResponse('send confirmation email')


def save_payment_info(request):
    return HttpResponse('save payment info')


def checkout(request):
    return HttpResponse('checkout')

