from django.contrib.auth.forms import UserCreationForm
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
            'email': TextInput(attrs={'class': 'form-control form-control-lg mb-4'}),
            'first_name': TextInput(attrs={'class': 'form-control form-control-lg mb-4'}),
            'last_name': TextInput(attrs={'class': 'form-control form-control-lg mb-4'}),
            'photo': FileInput()
        }
