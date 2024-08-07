from django import forms
from .models import ProductModel, ProductComment


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['name', 'email', 'Review_text']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'label': "your Name *",
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'label': "email *",
                'placeholder': 'Email'
            }),
            'Review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'label': "Review *",
                'placeholder': 'Review'
            })
        }









