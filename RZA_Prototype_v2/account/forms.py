from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models

class CustomerRegistrationForm(UserCreationForm): 
    class Meta:
        # Use the Account Model
        model = models.Account
        # These are the required fields
        fields = ['full_name', 'email', 'password1', 'password2']
        # Style the input boxes and add a placeholder to make it more clear
        widgets = {'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please enter your email'},),
                   'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your full name'},),}


class CustomerAuthenticationForm(AuthenticationForm):
    class Meta:
        # Use the Account Model
        model = models.Account
        # Style the input boxes and add a placeholder to make it more clear
        widgets = {'username': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please enter your email'},),
                   'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please enter your password'},),}
