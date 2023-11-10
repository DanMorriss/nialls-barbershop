from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from datetime import date
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, CreateView, UpdateView, ListView


class BookingsList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_system/booking-home.html'
    paginate_by = 25

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Booking.objects.filter(date_of_booking__gte=date.today()).order_by('date_of_booking', 'start_time')
            return queryset
        else:
            return Booking.objects.filter(username=self.request.user)
