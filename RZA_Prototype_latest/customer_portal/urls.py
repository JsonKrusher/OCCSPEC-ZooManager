from django.urls import path
from . import views


urlpatterns = [
    path('', views.customer_portal_page, name='customer_portal_page'),
    path('book/zoo-ticket', views.book_zoo_ticket, name='book_ticket_page'),
    path('ticket/delete/<int:ticket_id>', views.delete_zoo_ticket, name='book_ticket_page'),
    path('book/hotel-room', views.book_hotel_room, name='book_hotel_room'),
    path('book/hotel-room/delete/<int:booking_id>', views.delete_hotel_booking, name='delete_hotel_booking'),
]
