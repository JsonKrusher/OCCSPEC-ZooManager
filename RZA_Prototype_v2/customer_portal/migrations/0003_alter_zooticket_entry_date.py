# Generated by Django 4.2.3 on 2024-04-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0002_alter_zooticket_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zooticket',
            name='entry_date',
            field=models.DateField(),
        ),
    ]