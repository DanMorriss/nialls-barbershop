from .models import Booking
from django import forms
from datetime import datetime
from django.forms.widgets import DateInput


class BookingForm(forms.ModelForm):
    """For to create and edit a haircut booking"""
    class Meta:
        model = Booking
        fields = ["date_of_booking", "service_name", "start_time"]
        widgets = {'date_of_booking': DateInput(attrs={'type': 'date'}), }

        labels = {
            'date_of_booking': 'Date',
            'service_name': 'Haircut',
            'start_time': 'Time',
            }
