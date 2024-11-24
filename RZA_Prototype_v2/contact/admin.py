from django.contrib import admin
from . import models

# Register your models here.
# Register the ContactTicket model so that Support can see it in admin portal
admin.site.register(models.ContactTicket)
