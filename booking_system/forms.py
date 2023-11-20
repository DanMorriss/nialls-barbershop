from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import datetime, date
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form for creating and editing haircut bookings.

    Fields:
        - date_of_booking: Date field for selecting the booking date.
        - service_name: Dropdown for selecting the haircut service.
        - start_time: Time field for selecting the booking time.
        - message: A CharField for users to enter a message.

    Widgets:
        - date_of_booking: DateInput widget with type 'date' for a date picker.

    Labels:
        - date_of_booking: 'Date'
        - service_name: 'Haircut'
        - start_time: 'Time'
        - message: 'Message'

    Custom Clean Method:
        - Ensures that the selected date and time are in the future.
        - Checks for existing bookings and raises errors if there is a clash.

    Raises:
        - ValidationError: If the selected date is not in the future.
        - ValidationError: If the selected time is not in the future.
        - ValidationError: If the selected date and time are already booked.
    """
    class Meta:
        model = Booking
        fields = ["date_of_booking", "service_name", "start_time", 'message']
        widgets = {'date_of_booking': DateInput(attrs={'type': 'date'}), }

        labels = {
            'date_of_booking': 'Date',
            'service_name': 'Haircut',
            'start_time': 'Time',
            'message': 'Message'
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

        existing_bookings = Booking.objects.filter(
            date_of_booking=date_of_booking,
            start_time=start_time
        ).exclude(id=self.instance.id)

        if existing_bookings:
            raise ValidationError('That time is already taken, '
                                  'please select a different time.')


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
            raise ValidationError('Past dates not available in this universe.')


class SelectTimeForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time',]

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        date_of_booking = cleaned_data.get('date_of_booking')

        if start_time < datetime.now().time():
            raise ValidationError('Past dates not available in this universe.')

        existing_bookings = Booking.objects.filter(
            date_of_booking=date_of_booking,
            start_time=start_time
        )

        if existing_bookings:
            raise ValidationError('That time is already taken, '
                                  'please select a different time.')
