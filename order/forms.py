from django import forms
from django.forms import TextInput
from django_countries.fields import CountryField


class PaymentInfoForm(forms.Form):
    name = forms.CharField(max_length=300,
                           widget=forms.TextInput({'class': 'form-control form-control-lg mb-4',
                                                   'placeholder': 'Enter your full name',
                                                   'id': 'order-form-name'}))
    street_name = forms.CharField(max_length=300,
                                  widget=forms.TextInput({'class': 'form-control form-control-lg mb-4',
                                                          'placeholder': 'Enter your street name',
                                                          'id': 'order-form-street_name'}))
    house_number = forms.IntegerField(widget=forms.TextInput({
        'class': 'form-control form-control-lg mb-4',
        'placeholder': 'Enter your house number',
        'id': 'order-form-house_number'
    }))
    city = forms.CharField(max_length=300,
                           widget=forms.TextInput({'class': 'form-control form-control-lg mb-4',
                                                   'placeholder': 'Enter your city',
                                                   'id': 'order-form-city'}))
    postal_code = forms.CharField(max_length=100,
                                  widget=forms.TextInput({'class': 'form-control form-control-lg mb-4',
                                                          'placeholder': 'Enter your ZIP code',
                                                          'id': 'order-form-postal_code'}))
    country = CountryField().formfield(attr={'id': 'order-form-country'})

    name_of_cardholder = forms.CharField(max_length=300,
                                         widget=forms.TextInput({'class': 'form-control form-control-lg mb-4',
                                                                 'placeholder': 'Enter the name of the cardholder',
                                                                 'id': 'order-form-name_of_cardholder'}))
    card_number = forms.CharField(max_length=300,
                                  widget=forms.TextInput({'class': 'form-control form-control-lg mb-4',
                                                          'placeholder': 'Enter the card number',
                                                          'id': 'order-form-card_number'}))
    expiration_year = forms.IntegerField(widget=forms.NumberInput({'class': 'form-control form-control-lg mb-4',
                                                                   'placeholder': 'Year',
                                                                   'id': 'order-form-expiration_year'}))
    expiration_month = forms.IntegerField(widget=forms.NumberInput({'class': 'form-control form-control-lg mb-4',
                                                                   'placeholder': 'Month',
                                                                    'id': 'order-form-expiration_month'}))
    cvc = forms.IntegerField(widget=forms.TextInput({'class': 'form-control form-control-lg mb-4',
                                                     'placeholder': 'Enter the CVC number',
                                                     'id': 'order-form-cvc'}))
    save_info = forms.BooleanField()
