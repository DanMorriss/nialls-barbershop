# Generated by Django 3.2.22 on 2023-11-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0012_booking_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
