from django.db import models

# Create your models here.

class ContactTicket(models.Model):
    # This is the unique ID generated when a ticket is generated
    ticket_id = models.AutoField(primary_key=True)
    # Stores users full name
    full_name = models.TextField(max_length=64)
    # Stores users email address
    email = models.EmailField(max_length=64)
    # Support can mark when the ticket has been completed for anaylstics
    ticket_complete = models.BooleanField(default=False)
    # This is the message the user is sending
    ticket_content = models.TextField(max_length=512)

    def __str__(self):
        return f'{self.ticket_id} | {self.full_name} | Complete: {self.ticket_complete}'
