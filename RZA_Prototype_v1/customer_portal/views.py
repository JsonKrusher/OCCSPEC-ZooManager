from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from account import models as account_models
from . import forms
from datetime import date

# Create your views here.

@login_required(login_url="/account/login")
def customer_portal_page(request):
    try:
        tickets = models.ZooTicket.objects.filter(user_id=request.user)
        hotel_bookings = models.RoomBooking.objects.filter(user_id=request.user)
        context = {'tickets': tickets, 'bookings': hotel_bookings}
    except:
        context = {}

    return render(request, 'customer_portal/portal.html', context=context)

@login_required(login_url="/account/login")
def book_zoo_ticket(request):
    if request.method == 'POST':
        form = forms.BookZooTicketForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            entry_date = form.cleaned_data.get('entry_date')
            if entry_date < date.today():
                messages.error(request, 'The date cannot be in the past!')
                return redirect('customer_portal_page')

            form.save()
            messages.success(request, f'Booked Ticket. Valid for entry on {entry_date}')
            return redirect('customer_portal_page')
        
                

    form = forms.BookZooTicketForm
    return render(request, 'customer_portal/book-ticket.html', context={'form': form}) 

@login_required(login_url="/account/login")
def delete_zoo_ticket(request, ticket_id):
    ticket = models.ZooTicket.objects.get(ticket_id=ticket_id)

    if not request.user == ticket.user:
        messages.error(request, 'You do not have permission to perform this action!')
        return redirect('customer_portal_page')

    ticket.delete()
    messages.success(request, 'Zoo Ticket was deleted!')
    
    return redirect('customer_portal_page')

@login_required(login_url="/account/login")
def book_hotel_room(request):
    if request.method == 'POST':
        form = forms.BookHotelRoomForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            hotel_room = form.cleaned_data.get('room_id')


            if form.cleaned_data.get('guests') > hotel_room.max_guests:
                messages.error(request, 'You have selected too many guests for the room!')
                return redirect('book_hotel_room')            
            
            booking_in = form.cleaned_data.get('booking_in')
            booking_out = form.cleaned_data.get('booking_in')

            if booking_in < date.today() or booking_out < date.today() or booking_out < booking_in:
                messages.error(request, 'The date cannot be in the past!')
                return redirect('book_hotel_room')
            
            check_booking = models.RoomBooking.objects.filter(
                room_id=hotel_room.room_id,
                booking_in__lt=booking_in,
                booking_out__gt=booking_out
            )

            if check_booking.exists() == True:
                messages.error(request, f'This room is booked! Current Bookings for room:')
                for i, o in check_booking.get('booking_in'), check_booking.get('booking_out'):
                    print(i, o)
                return redirect('book_hotel_room')
            
            form.save()
            messages.success(request, f'Booked Room {hotel_room.room_id} {booking_in}/{booking_out}')

            

    form = forms.BookHotelRoomForm
    return render(request, 'customer_portal/hotel-booking.html', {'form': form})

@login_required(login_url="/account/login")
def delete_hotel_booking(request, booking_id):
    booking_id = models.RoomBooking.objects.get(booking_id=booking_id)

    if not request.user == booking_id.user:
        messages.error(request, 'You do not have permission to perform this action!')
        return redirect('customer_portal_page')

    booking_id.delete()
    messages.success(request, 'Hotel Booking was deleted!')

    return redirect('customer_portal_page')