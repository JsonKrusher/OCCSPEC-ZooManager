# Generated by Django 4.2.3 on 2024-04-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0004_rename_account_id_roombooking_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='booking_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='booking_out',
            field=models.DateField(),
        ),
    ]
