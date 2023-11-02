from django.shortcuts import render
from django.views import generic
from .models import Booking
from datetime import date


class BookingsList(generic.ListView):
    model = Booking
    template_name = 'index.html'
    paginate_by = 25
    queryset = Booking.objects.filter(date_of_booking__gte=date.today()).order_by('date_of_booking', 'start_time')
