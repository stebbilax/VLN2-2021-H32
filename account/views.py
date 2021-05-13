from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginForm, EditAccountForm
from .decorators import check_if_user_exists
from .models import Account, SearchHistoryEntry


@login_required(login_url='login')
def account_page(request):
    """
    Handles GET and POST requests to the account page.
    If GET display the stored account information.
    If POST update the account information
    """
    account = Account.objects.get(user=request.user)
    account_form = EditAccountForm(instance=account)

    if request.method == 'POST':
        form = EditAccountForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account')

    user_obj = {'img': account.photo_url}

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
def search_history_page(request):
    """ Displays the users previous searches """
    search_history = SearchHistoryEntry.objects.filter(account=request.user.account)
    context = {'search_history': search_history}
    return render(request, 'account/search_history.html', context)


@login_required(login_url='login')
def logout_user(request):
    """ Logout function """
    logout(request)
    return redirect('home')


@check_if_user_exists
def create_account(request):
    """ Handles user creation process """
    if request.user.is_authenticated:
        return redirect('account')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            password1 = form.data['password1']
            password2 = form.data['password2']
            email = form.data['email']
            for msg in form.errors.as_data():
                if msg == 'email':
                    messages.error(request, f"Declared {email} is not valid")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, f"Selected password is not strong enough, please try again.")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request, f"Password and Password Confirmation do not match, please try again.")

    context = {"form": form}
    return render(request, 'account/create_user.html', context)


@login_required(login_url='login')
def delete_account(request):
    """ Handles account deletion """
    if request.method == 'POST':
        if not request.user.has_perm('auth.view_user'):
            the_account = Account.objects.get(user=request.user)
            the_account.delete()
            request.user.delete()
            return redirect('logout')
    return render(request, 'account/delete.html')



