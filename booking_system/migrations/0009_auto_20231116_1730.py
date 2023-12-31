# Generated by Django 3.2.22 on 2023-11-16 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking_system', '0008_booking_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_name_booking', to='booking_system.services'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username_booking', to=settings.AUTH_USER_MODEL),
        ),
    ]
