from django import forms
from django.contrib.auth.models import User
from .models import profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=profile.user_type)

    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']
