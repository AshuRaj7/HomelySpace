from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        