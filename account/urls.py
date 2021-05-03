from django.urls import path, include
from .views import (account_page, login_page, logout_user,
                    reset_password, create_account)

urlpatterns = [
    path('', account_page, name='account'),
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('reset_password', reset_password, name='reset_password'),
    path('create', create_account, name='create_account')
]
