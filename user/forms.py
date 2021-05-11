from django import forms


class ContactEmailForm(forms.Form):
    name = forms.CharField(max_length=300, widget=forms.TextInput({
        'class': 'form-control form-control-lg mb-4',
        'placeholder': 'Enter your full name'
    }))
    email = forms.EmailField(widget=forms.EmailInput({
        'class': 'form-control form-control-lg mb-4',
        'placeholder': 'Enter your email'
    }))
    message = forms.CharField(max_length=1000, widget=forms.Textarea({
        'class': 'form-control form-control-lg mb-4',
        'placeholder': 'Enter your message'
    }))