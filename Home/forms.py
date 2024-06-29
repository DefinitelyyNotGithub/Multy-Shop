from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['seen', ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Name"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Email"
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "subject"
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Message"
            }),
        }
