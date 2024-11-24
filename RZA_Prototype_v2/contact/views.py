from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

# Create your views here.

def contact_page(request):
    # Check if the user is sending data to the server
    if request.method == 'POST':
        # Grab the form and data filled in by user
        form = forms.ContactForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the form
            form.save()
            # Alert the user
            messages.success(request, 'You message was sent!')
            # Redirect back to the contact page to show alert
            redirect('contact_page')
        else:
            # If the form is not valid
            # Alert the user
            messages.error(request, 'Error sending contact information.')
            # Redirect back to the contact page to show alert
            redirect('contact_page')
    # If the user is not using POST we can send them the form
    # Grab the form froms form.py
    form = forms.ContactForm
    # Render the form to the user
    return render(request, 'contact/contact_form.html', {'form': form})
