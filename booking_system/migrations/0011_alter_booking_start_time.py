# Generated by Django 3.2.22 on 2023-11-19 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0010_merge_0009_auto_20231116_1634_0009_auto_20231116_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(choices=[(datetime.time(9, 0), '9:00am'), (datetime.time(9, 30), '9:30am'), (datetime.time(10, 0), '10:00am'), (datetime.time(10, 30), '10:30am'), (datetime.time(11, 0), '11:00am'), (datetime.time(11, 30), '11:30am'), (datetime.time(12, 0), '12:00pm'), (datetime.time(12, 30), '12:30pm'), (datetime.time(13, 0), '1:00pm'), (datetime.time(13, 30), '1:30pm'), (datetime.time(14, 0), '2:00pm'), (datetime.time(14, 30), '2:30pm'), (datetime.time(15, 0), '3:00pm'), (datetime.time(15, 30), '3:30pm'), (datetime.time(16, 0), '4:00pm'), (datetime.time(16, 30), '4:30pm')]),
        ),
    ]
