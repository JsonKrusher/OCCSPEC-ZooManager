# Generated by Django 4.2.3 on 2024-04-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactticket',
            name='ticket_complete',
            field=models.BooleanField(default=False),
        ),
    ]
