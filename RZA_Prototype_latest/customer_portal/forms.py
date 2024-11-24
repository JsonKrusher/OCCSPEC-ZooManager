from django import forms
from django.forms import ModelForm
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