# Generated by Django 3.2.22 on 2023-11-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0003_alter_booking_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(blank=True, editable=False, null=True),
        ),
    ]
