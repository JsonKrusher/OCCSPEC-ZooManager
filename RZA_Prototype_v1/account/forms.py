from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from . import models

class CustomerRegistrationForm(UserCreationForm): 
    class Meta:
        model = models.Account
        fields = ('full_name', 'email', 'password1', 'password2')


class CustomerAuthenticationForm(AuthenticationForm):
    class Meta:
        model = models.Account