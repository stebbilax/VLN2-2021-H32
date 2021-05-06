from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginForm, EditAccountForm
from .decorators import check_if_user_exists


#   GET - get account info
#   POST / PATCH / PUT - change account info
#   DELETE - Delete account


@login_required(login_url='login')
def account_page(request):
    return HttpResponse('Account page')


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


def edit_account(request):
    def get_object(self):
        return self.request.user

    form = EditAccountForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/account/')

        else:
            form = EditAccountForm(instance=request.user)
            args = {'form': form}
            return render(request, 'account/edit_account.html', args)
    args = {'form': form}
    return render(request, 'account/edit_account.html', args)




