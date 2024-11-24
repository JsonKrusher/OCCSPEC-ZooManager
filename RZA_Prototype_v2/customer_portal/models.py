from django.db import models
from account import models as account_model

# Create your models here.

class ZooTicket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(account_model.Account, on_delete=models.CASCADE)
    entry_date = models.DateField()
    ticket_used = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.ticket_id} | {self.user.full_name} | {self.entry_date} | {self.ticket_used}"
    

class HotelRoom(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_description = models.CharField(max_length=128)
    max_guests = models.IntegerField()
    room_reserved = models.BooleanField()

    def __str__(self) -> str:
        return f"Room {self.room_id} | {self.room_description} | Max Guests {self.max_guests} | Room Reserved: {self.room_reserved}"


class RoomBooking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(account_model.Account, on_delete=models.CASCADE)
    room_id = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    guests = models.IntegerField()
    booking_in = models.DateField()
    booking_out = models.DateField()

    def __str__(self) -> str:
        return f"Booking: {self.booking_id} | Full Name: {self.user.full_name} | Guests: {self.guests}/{self.room_id.max_guests} | {self.booking_in}-{self.booking_out}"


