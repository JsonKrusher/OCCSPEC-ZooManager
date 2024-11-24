from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms
from . import models

# Create your views here.

def login_page(request):
    # If the user is authenticated they do not need to login
    if request.user.is_authenticated:
        return redirect('customer_portal_page')

    # Check if the user is sending data to server
    if request.method == 'POST':
        # Grab login form and data sent
        login_form = forms.CustomerAuthenticationForm(request, data=request.POST)
        # Check if the data sent is valid
        if login_form.is_valid():
            # As it using a Custom Authentication Form it will send the email as username
            email = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            # Attempt to authenticate the user
            customer = authenticate(request, email=email, password=password)
            # If the user is authenticated
            if customer is not None:
                messages.success(request, 'Login Success!')
                login(request, user=customer)
                return redirect('customer_portal_page')
        # We know the user is not authenticated so incorrect details
        messages.warning(request, 'Invalid Login Details!')
        return redirect('login_page')
    else:
        # Send login form to user
        login_form = forms.CustomerAuthenticationForm(request)
        return render(request, 'account/login.html', {'form': login_form})

def register_page(request):
    # If the user is authenticated they do not need to register
    if request.user.is_authenticated:
        return redirect('customer_portal_page')

    # Check if the user is sending data to server
    if request.method == 'POST':
        # Grab register form and data sent
        register_form = forms.CustomerRegistrationForm(data=request.POST)
        #print("Recv request")
        
        if register_form.is_valid():
            #print("Form valid!")
            full_name = register_form.cleaned_data.get('full_name')
            email = register_form.cleaned_data.get('email')
            
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')

            # Check if passwords don't match
            if password1 != password2:
                messages.warning(request, 'The passwords should match!')
                return redirect('register_page')
    
            # See if email already exists
            get_email_db = models.Account.objects.filter(email=email).exists()

            # If email does return error
            if get_email_db:
                messages.warning(request, 'This email already exists!')
                return redirect('register_page')

            # All is good - create the new user
            new_customer = models.Account.objects.create_user(
                full_name = full_name,
                email=email        
            )
            # Set the password 
            new_customer.set_password(password1)
            # Save the new user
            new_customer.save()
            # Alert the user of account create
            messages.success(request, 'Account Created!')
            return redirect('login_page')
        else:
            # We know the form is invalid so throw an error
            messages.warning(request, 'Either the email is already in use or your passwords do not match!')
            return redirect('register_page')
    else:
        # Render form
        reigster_form = forms.CustomerRegistrationForm
        return render(request, 'account/register.html', {'form': reigster_form})

def logout_function(request):
    # If the user is authenticated can login
    if request.user.is_authenticated:
        # Logout the user and flush their session
        logout(request)
        # Alert user
        messages.success(request, 'You have been logged out!')
    else:
        # If the user is not logged in they shouldnt be able to logout
        # Alert the user
        messages.warning(request, 'You need to be logged in to do that!')
    
    # Redirect back to the login page
    return redirect('login_page')