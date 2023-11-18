from .models import Booking, Services, BOOKING_TIME
from django import forms
from datetime import datetime, date
from django.utils import timezone
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

    def clean(self):
        cleaned_data = super().clean()
        date_of_booking = cleaned_data.get('date_of_booking')
        start_time = cleaned_data.get('start_time')

        if date_of_booking and date_of_booking < date.today():
            raise ValidationError('Please select a date in the future.')

        if date_of_booking == date.today() and \
                start_time < datetime.now().time():
            raise ValidationError('Please select a time in the future.')


# Form Wizard Forms
class SelectHaircutForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service_name',]
        widgets = {'service_name': forms.Select()}


class SelectDateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date_of_booking',]
        widgets = {'date_of_booking': DateInput(attrs={'type': 'date'})}

    def clean(self):
        cleaned_data = super().clean()
        date_of_booking = cleaned_data.get('date_of_booking')

        if date_of_booking and date_of_booking < date.today():
            raise ValidationError('Please select a date in the future.')


class SelectTimeForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time',]
