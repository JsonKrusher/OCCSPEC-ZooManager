# Generated by Django 4.2.3 on 2024-04-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactTicket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.TextField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('ticket_content', models.TextField(max_length=512)),
            ],
        ),
    ]
