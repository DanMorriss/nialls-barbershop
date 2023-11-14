from .models import Booking, BOOKING_TIME
from django import forms
from datetime import datetime
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    """
    Form to create and edit a haircut booking.

    Fields:
        - date_of_booking: Date field for selecting the booking date.
        - service_name: Dropdown for selecting the haircut service.
        - start_time: Time field for selecting the booking time.

    Widget:
        - date_of_booking: DateInput widget with type 'date' for a date picker.

    Labels:
        - date_of_booking: 'Date'
        - service_name: 'Haircut'
        - start_time: 'Time'
    """
    class Meta:
        model = Booking
        fields = ["date_of_booking", "service_name", "start_time"]
        widgets = {'date_of_booking': DateInput(attrs={'type': 'date'}), }

        labels = {
            'date_of_booking': 'Date',
            'service_name': 'Haircut',
            'start_time': 'Time',
            }


class SelectHaircut(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date_of_booking", "service_name",]
        widgets = {'date_of_booking': DateInput(attrs={'type': 'date'}),
                   'service_name': forms.HiddenInput(), }

        labels = {
            'date_of_booking': 'Date',
            'service_name': 'Haircut',
            }
