from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

# Create your views here.

def contact_page(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You message was sent!')
        else:
            messages.error(request, 'Error sending contact information.')
            redirect('contact_page')
    
    form = forms.ContactForm
    return render(request, 'contact/contact_form.html', {'form': form})
