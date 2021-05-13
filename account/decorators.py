from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect


def check_if_user_exists(view_func):
    """
    Checks if username already exists and if so displays a error message
    and redirects user back to the create_account page
    """
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('create_account')
        return view_func(request, *args, **kwargs)
    return wrapper
