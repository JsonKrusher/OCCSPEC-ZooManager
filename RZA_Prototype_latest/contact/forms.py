from django import forms
from django.forms import ModelForm
from . import models


class ContactForm(ModelForm):
    class Meta:
        # Use the ContactTicket Table from Models
        model = models.ContactTicket
        # Get all the fields
        fields = '__all__'
        # Exclude ticket_id as this is auto-generated and should be unique
        # Also exclude the ticket complete field as it should only be changed by support staff
        exclude = ['ticket_id', 'ticket_complete']
        # Use Widgets to add custom placeholders on each input for accessability
        widgets = {'email': forms.EmailInput(attrs={'placeholder':'Please enter your email'},),
                   'full_name': forms.TextInput(attrs={'placeholder':'Please enter your full name'},),
                   'ticket_content': forms.TextInput(attrs={'placeholder':'Please enter your message'},),}
