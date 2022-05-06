from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from customer.models import Orders
from customer.models import Profile


class FeedbackForm(forms.Form):
    product_name = forms.CharField()
    feedback = forms.CharField()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["address"]
        widgets = {
            'address': forms.Textarea(attrs={"class": "form-control"}),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=["address","phone_number","profile_pic",]
        widgets = {
            "address": forms.Textarea(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "profile_pic": forms.FileInput(attrs={"class": "form-control"}),
        }


# class RegistrationForm(forms.Form):
#     first_name=forms.CharField()
#     last_name=forms.CharField()
#     email=forms.CharField()
#     phone=forms.CharField()
#     username=forms.CharField()
#     password=forms.CharField(widget=forms.PasswordInput())
