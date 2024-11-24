from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ZooTicket)
admin.site.register(models.HotelRoom)
admin.site.register(models.RoomBooking)