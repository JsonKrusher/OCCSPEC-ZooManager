from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms
from . import models

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        redirect('customer_portal_page')

    if request.method == 'POST':
        login_form = forms.CustomerAuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            customer = authenticate(request, email=email, password=password)
            if customer is not None:
                messages.success(request, 'Login Success!')
                login(request, user=customer)
                return redirect('customer_portal_page')
            else:
                messages.error(request, 'Your Email or Password is incorrect!')
        return redirect('login_page')
    else:
        login_form = forms.CustomerAuthenticationForm(request)
        return render(request, 'account/login.html', {'form': login_form})

def register_page(request):
    if request.user.is_authenticated:
        redirect('customer_portal_page')

    if request.method == 'POST':
        register_form = forms.CustomerRegistrationForm(data=request.POST)
        #print("Recv request")
        if register_form.is_valid():
            #print("Save form!")
            full_name = register_form.cleaned_data.get('full_name')
            email = register_form.cleaned_data.get('email')

            if models.Account.objects.filter(email=email).exists():
                messages.error(request, 'This email already exists!')
                return redirect('register_page')

            password = register_form.cleaned_data.get('password1')

            new_customer = models.Account.objects.create_user(
                full_name = full_name,
                email=email        
            )
            new_customer.set_password(password)
            new_customer.save()
            return redirect('login_page')
        else:
            redirect('register_page')
    else:
        reigster_form = forms.CustomerRegistrationForm
        return render(request, 'account/register.html', {'form': reigster_form})

def logout_function(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out!')
    else:
        messages.error(request, 'You need to be logged in to do that!')
    
    return redirect('login_page')