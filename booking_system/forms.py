from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ("date_of_booking", "service_name", "start_time",)