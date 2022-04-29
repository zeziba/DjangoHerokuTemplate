# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account

class UserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ("username", "email")

class UserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ("username", "email")