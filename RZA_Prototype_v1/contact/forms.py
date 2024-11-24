from django import forms
from django.forms import ModelForm
from . import models


class ContactForm(ModelForm):
    class Meta:
        model = models.ContactTicket
        fields = '__all__'
