
from dataclasses import fields
from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import User
from  .models import*

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class StatistikaForm(forms.ModelForm):
    class Meta:
        model = CategoryUser
        fields = '__all__'