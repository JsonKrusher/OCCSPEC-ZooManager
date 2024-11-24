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
        # Filter for any tickets the current user has
        tickets = models.ZooTicket.objects.filter(user_id=request.user)
        # Filter for any hotel bookings the curretn user has
        hotel_bookings = models.RoomBooking.objects.filter(user_id=request.user)
        # Add each to context
        context = {'tickets': tickets, 'bookings': hotel_bookings}
    except:
        context = {}

    # Render the page and send the data
    return render(request, 'customer_portal/portal.html', context=context)

@login_required(login_url="/account/login")
def book_zoo_ticket(request):
    if request.method == 'POST':
        form = forms.BookZooTicketForm(request.POST)
        if form.is_valid():
            # Set the user
            form.instance.user = request.user
            entry_date = form.cleaned_data.get('entry_date')
            # Check if date is in the past
            if entry_date < date.today():
                messages.warning(request, 'The date cannot be in the past!')
                return redirect('customer_portal_page')
            # Save ticket
            form.save()
            messages.success(request, f'Booked Ticket. Valid for entry on {entry_date}')
            return redirect('customer_portal_page')
        
                

    form = forms.BookZooTicketForm
    return render(request, 'customer_portal/book-ticket.html', context={'form': form}) 

@login_required(login_url="/account/login")
def delete_zoo_ticket(request, ticket_id):
    # Get ticket id
    ticket = models.ZooTicket.objects.get(ticket_id=ticket_id)

    # Check if user can delete the ticket
    if not request.user == ticket.user:
        messages.warning(request, 'You do not have permission to perform this action!')
        return redirect('customer_portal_page')

    # Delete ticket
    ticket.delete()
    messages.success(request, 'Zoo Ticket was deleted!')
    
    return redirect('customer_portal_page')

@login_required(login_url="/account/login")
def book_hotel_room(request):
    if request.method == 'POST':
        # Get form and data from it 
        form = forms.BookHotelRoomForm(data=request.POST)
        if form.is_valid():
            # Set the user
            form.instance.user = request.user
            hotel_room = form.cleaned_data.get('room_id')

            # Check if too many guests
            if form.cleaned_data.get('guests') > hotel_room.max_guests:
                messages.warning(request, 'You have selected too many guests for the room!')
                return redirect('book_hotel_room')            
            
            booking_in = form.cleaned_data.get('booking_in')
            booking_out = form.cleaned_data.get('booking_in')

            # Check if book is today or in the future or the booking out is before the booking in
            if booking_in < date.today() or booking_out < date.today() or booking_out < booking_in:
                messages.warning(request, 'The date cannot be in the past!')
                return redirect('book_hotel_room')
            
            # Filter to see if the booking exists
            check_booking = models.RoomBooking.objects.filter(
                room_id=hotel_room.room_id,
                booking_in__lt=booking_in,
                booking_out__gt=booking_out
            )

            # If the booking exists send error
            if check_booking.exists() == True:
                messages.warning(request, f'This room is booked for that date!')
                return redirect('book_hotel_room')
            
            # Save the from
            form.save()
            # Alert the user
            messages.success(request, f'Booked Room {hotel_room.room_id} {booking_in}/{booking_out}')
            return redirect('customer_portal')
    else:
        # Get booking form and render it 
        form = forms.BookHotelRoomForm
        return render(request, 'customer_portal/hotel-booking.html', {'form': form})

@login_required(login_url="/account/login")
def delete_hotel_booking(request, booking_id):
    # Get booking id
    booking_id = models.RoomBooking.objects.get(booking_id=booking_id)

    # Check if user is meant to be able to deleted
    if not request.user == booking_id.user:
        messages.warning(request, 'You do not have permission to perform this action!')
        return redirect('customer_portal_page')

    # Delete it
    booking_id.delete()
    # Alert user
    messages.success(request, 'Hotel Booking was deleted!')

    return redirect('customer_portal_page')