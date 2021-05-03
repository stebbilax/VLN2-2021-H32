from django.shortcuts import render, HttpResponse, redirect

from .forms import CreateUserForm
from .decorators import check_if_user_exists


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



@check_if_user_exists
def create_account(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form}
    return render(request, 'account/create_user.html', context)
