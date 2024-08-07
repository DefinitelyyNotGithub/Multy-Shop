from django import forms
from Account.models import UserShippingAddress


class AddressForm(forms.ModelForm):
    class Meta:
        model = UserShippingAddress
        exclude = ['user', ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "john"
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Doe"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "example@gmail.com"
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "+123 456 789"
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "New York"
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "New York"
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "123"
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "address..."
            }),

        }
