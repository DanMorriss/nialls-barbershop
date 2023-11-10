from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from datetime import date
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy


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


class CreateBooking(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'booking_system/create-booking.html'
    success_url = reverse_lazy('booking_home')
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
