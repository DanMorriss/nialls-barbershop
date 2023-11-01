# Generated by Django 3.2.22 on 2023-11-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(choices=[('09:00:00', '9:00am'), ('09:15:00', '9:15am'), ('09:30:00', '9:30am'), ('09:45:00', '9:45am')]),
        ),
        migrations.AlterField(
            model_name='services',
            name='session_length',
            field=models.DurationField(),
        ),
    ]
