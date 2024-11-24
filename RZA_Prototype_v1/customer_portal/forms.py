from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from . import models



class BookZooTicketForm(ModelForm):
    class Meta:
        model = models.ZooTicket
        exclude = ['user', 'ticket_id', 'ticket_used']
        # Help provided from https://stackoverflow.com/questions/49440853/django-2-0-modelform-datefield-not-displaying-as-a-widget
        widgets = {'entry_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a entry date', 'type':'date'},),}

class BookHotelRoomForm(ModelForm):
    class Meta:
        model = models.RoomBooking
        exclude = ['booking_id', 'user']
        widgets = {'booking_in': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a booking in date', 'type':'date'},),
                   'booking_out': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a booking out date', 'type':'date'},),}