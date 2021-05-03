from django.shortcuts import render, HttpResponse


# Create your views here.
#   GET - get account info
#   POST / PATCH / PUT - change account info
#   DELETE - Delete account
def account_page(request):
    return HttpResponse('Account page')


def login_page(request):
    return HttpResponse('Login page')


def logout(request):
    return HttpResponse('Logout')


def reset_password(request):
    return HttpResponse('Reset password')


