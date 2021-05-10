from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import PaymentInfoForm


# Create your views here.
def index(request):
    payment_form = PaymentInfoForm()

    context = {'form': payment_form }
    return render(request, 'order/order.html', context)


def place_order(request):
    return HttpResponse('place order')


def send_confirmation_email(request):
    return HttpResponse('send confirmation email')


def save_payment_info(request):
    return HttpResponse('save payment info')


def checkout(request):
    return HttpResponse('checkout')

