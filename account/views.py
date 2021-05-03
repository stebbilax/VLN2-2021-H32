from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import CreateUserForm, LoginForm
from .decorators import check_if_user_exists


#   GET - get account info
#   POST / PATCH / PUT - change account info
#   DELETE - Delete account
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


def logout_user(request):
    """ Logout function """
    logout(request)
    return redirect('home')


def reset_password(request):
    return HttpResponse('Reset password')


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
