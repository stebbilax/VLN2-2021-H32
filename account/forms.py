from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django import forms
from django.forms import TextInput, FileInput
from django.contrib.auth.models import User

from .models import Account


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control form-control-lg mb-4",
               'id': "inputEmail"
               }
    ))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': "form-control form-control-lg mb-4",
               'id': "inputPassword"
               }
    ))


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'email',
            'first_name',
            'last_name',
            'photo'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg mb-4'}),
            'first_name': TextInput(attrs={'class': 'form-control form-control-lg mb-4'}),
            'last_name': TextInput(attrs={'class': 'form-control form-control-lg mb-4'}),
            'photo': FileInput()
        }


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg mb-3',
        'placeholder': 'Email',
        'type': 'email',
        'name': 'email'
    }))
