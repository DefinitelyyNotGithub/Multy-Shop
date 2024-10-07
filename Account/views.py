import random
import uuid
import ghasedakpack
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView

from .forms import UserLogInForm, InitialUserCreationForm, ValidationCodeForm, UserProfileShippingSettingsForm, \
    UserProfileForm

from .models import User, RegisterModel
from random import randint

sms = ghasedakpack.Ghasedak("ab58d879f41092f867eef403f3fffa3587d6db979b9958cc3a2dcdec16f9ce4f")


class UserLogInView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = UserLogInForm(request.GET)
        return render(request, 'Account/Login.html', {'form': form})

    def post(self, request):
        form = UserLogInForm(request.POST)

        if form.is_valid():
            Phone_number, password = form.cleaned_data.get('Phone_number'), form.cleaned_data.get('Password')
            user = authenticate(username=Phone_number, password=password)
            if user is not None:
                login(request, user)
                if request.session['favorites']:
                    for item in request.session['favorites']:
                        pass

                if request.get('next'):
                    return redirect(request.get('next'))
                return redirect('Home:home')
            else:
                form.add_error("__all__", "phone number or password is wrong")
        return render(request, 'Account/Login.html', {'form': form})


def Logout(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = InitialUserCreationForm(request.GET)
        return render(request, 'Account/Register.html', {'form': form})

    def post(self, request):
        form = InitialUserCreationForm(request.POST)
        if form.is_valid():
            Rc = random.randint(100000, 999999)
            token = uuid.uuid4()
            cd = form.cleaned_data
            if User.objects.get(phone=cd['phone_number']).exists():
                form.add_error('__all__', "This number is already registered !")
            else:
                try:
                    sms.verification(
                        {'receptor': form.phone_number, 'type': '1', 'template': 'python', 'param1': Rc})
                except:
                    form.add_error('phone_number', "invalid Phone number !")

                else:
                    sms.verification(
                        {'receptor': cd['phone_number'], 'type': '1', 'template': 'python', 'param1': Rc})
                    RegisterModel.objects.create(phone=cd['phone_number'], password=cd['password'], random_code=Rc,
                                                 token=token)
                    return redirect(reverse('Account:code validation') + f'?token={token}')


class CodeValidation(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = InitialUserCreationForm(request.POST)
        return render(request, 'Account/validationcode.html', {'form': form})

    def post(self, request):
        form = ValidationCodeForm(request.POST)
        token = request.POST.get('token')
        if form.is_valid():
            if RegisterModel.objects.get(token=token, random_code=form.cleaned_data.get('code')).exists():
                obj = RegisterModel.objects.get(token=token)
                user = User.objects.create_user(password=obj.password, phone=obj.phone)
                login(request, user)
                obj.delete()
                obj.save()
                return redirect('/')
        return render(request, 'Account/validationcode.html', {'form': form})


class AddShippingAddress(CreateView):
    template_name = 'Account/add_shipping_address.html'
    form_class = UserProfileShippingSettingsForm

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect(self.request.META.get('HTTP_REFERER', '/'))


class UserProfile(CreateView):
    template_name = 'Account/user-profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('Home:home')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
