from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core import validators
from django.core.exceptions import ValidationError
from django import forms
from .models import User, UserShippingAddress, UserProfile


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["phone", ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone", "password", "is_active", "is_admin"]


class UserLogInForm(forms.Form):
    Phone_number = forms.CharField(validators=[validators.MinLengthValidator(11), validators.MaxLengthValidator(11)],
                                   widget=
                                   forms.TextInput(attrs={
                                       "class": "form-control",
                                       "placeholder": "Phone Number"
                                   }))
    Password = forms.CharField(validators=[validators.MaxLengthValidator(16), validators.MinLengthValidator(4)],
                               widget=
                               forms.PasswordInput(attrs={
                                   "class": "form-control",
                                   "placeholder": "Password"
                               }))


class InitialUserCreationForm(forms.Form):
    phone_number = forms.CharField(validators=[validators.MinLengthValidator(11), validators.MaxLengthValidator(11)],
                                   widget=
                                   forms.TextInput(attrs={
                                       "class": "form-control",
                                       "placeholder": "Phone number"
                                   }))

    password = forms.CharField(validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(16)],
                               widget=
                               forms.PasswordInput(attrs={
                                   "class": "form-control",
                                   "placeholder": "Password"
                               }))

    password_confirm = forms.CharField(
        widget=
        forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "confirm Password"
        }))

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_confirm'):
            raise ValidationError("Not the same Passwords!")


class ValidationCodeForm(forms.Form):
    code = forms.CharField(validators=[validators.MinLengthValidator(6), validators.MaxLengthValidator(6)],
                           widget=
                           forms.TextInput(attrs={
                               "class": "form-control",
                               "placeholder": "Enter Code"
                           }))


class UserProfileShippingSettingsForm(forms.ModelForm):
    class Meta:
        model = UserShippingAddress
        exclude = ['user', ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "First Name "

            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Last Name ",
                'label': "last name"
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': "email ",
                'label': "Email Address"
            }),
            'phone_number': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "phone number ",
                'label': "Telephone Number"
            }),
            'city': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "city ",
                'label': "City"
            }),
            'state': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "state ",
                'label': "State OR City"
            }),
            'zip_code': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Zip code ",
                'label': "Zip Code"
            }),
            'address': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Address",
                'label': "Full Address"
            }),

        }

        labels = {
            'first_name': 'Firs Name',
            'last_name': "Last Name",
            'email': 'Email Address',
            'phone_number': "Telephone Number",
            'city': 'City',
            'state': 'City or State',
            'zip_code': "Zip Code",
            'Address': "Full Address"
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model: UserProfile
        exclude = ['user', ]

        widgets = {
            'profile_pic': forms.ImageField(),
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'User Name'
            })
        }
