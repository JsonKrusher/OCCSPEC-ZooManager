from django.db import models

# Create your models here.

class ContactTicket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    full_name = models.TextField(max_length=64)
    email = models.EmailField(max_length=64)
    ticket_complete = models.BooleanField(default=False)
    ticket_content = models.TextField(max_length=512)

    def __str__(self):
        return f'{self.ticket_id} | {self.full_name} | Complete: {self.ticket_complete}'
