from datetime import datetime
import re
from django import forms
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
    postal_code = forms.IntegerField(widget=forms.TextInput({'class': 'form-control form-control-lg mb-4',
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
    save_info = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput({'class': 'form-check-input ms-0',
                                                                'type': 'checkbox',
                                                                'value': ''}))

    def clean_expiration_year(self):
        expiration_year = self.cleaned_data.get("expiration_year")
        if not expiration_year >= datetime.now().year:
            raise forms.ValidationError("The expiration year cannot be in the past")

        return expiration_year

    def clean_expiration_month(self):
        expiration_month = self.cleaned_data.get('expiration_month')
        if not 1 <= expiration_month <= 12:
            raise forms.ValidationError("Must be a valid month 1-12")

        return expiration_month

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        visa_pattern = r'^4[0-9]{12}(?:[0-9]{3})?$'
        mastercard_pattern = r'^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$'
        american_express_pattern = r'^3[47][0-9]{13}$'
        discover_pattern = r'^6(?:011|5[0-9]{2})[0-9]{12}$'

        p1 = re.compile(visa_pattern)
        p2 = re.compile(mastercard_pattern)
        p3 = re.compile(american_express_pattern)
        p4 = re.compile(discover_pattern)
        if not p1.match(card_number) and not p2.match(card_number) and not p3.match(card_number) and not p4.match(
                card_number):
            raise forms.ValidationError("Please enter a valid credit card number")

        return card_number
