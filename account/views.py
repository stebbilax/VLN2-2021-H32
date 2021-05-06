from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginForm, EditAccountForm
from .decorators import check_if_user_exists
from .models import Account


@login_required(login_url='login')
def account_page(request):
    account = Account.objects.get(user=request.user)
    account_form = EditAccountForm(instance=account)

    if request.method == 'POST':
        form = EditAccountForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account')

    user_obj = {'img': account.photo.url}

    context = {'user_obj': user_obj, 'user_form': account_form}
    return render(request, 'account/account_page.html', context)


def login_page(request):
    """ Renders a login form and authenticates users """
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {'form': form}
    return render(request, 'account/login.html', context)


@login_required(login_url='login')
def logout_user(request):
    """ Logout function """
    logout(request)
    return redirect('home')


@check_if_user_exists
def create_account(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {"form": form}
    return render(request, 'account/create_user.html', context)





