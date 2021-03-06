from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (account_page, login_page, logout_user,
                    create_account, search_history_page, delete_account)
from .forms import UserPasswordResetForm, UserSetPasswordForm

urlpatterns = [
    path('', account_page, name='account'),
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('create', create_account, name='create_account'),
    path('search_history', search_history_page, name='search_history'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password/password_reset_confirm.html',
        form_class=UserSetPasswordForm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='password/password_reset.html',
        form_class=UserPasswordResetForm), name='reset_password'),
    path('delete/', delete_account, name='account_delete')
]

