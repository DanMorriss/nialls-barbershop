from django.shortcuts import render
from django.views import generic
from .models import Booking
from datetime import date
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, CreateView, UpdateView, ListView


class BookingsList(generic.ListView):
    model = Booking
    template_name = 'account-home.html'
    paginate_by = 25
    queryset = Booking.objects.filter(date_of_booking__gte=date.today()).order_by('date_of_booking', 'start_time')


class CreateBookingView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking.html'
    success_url = "/booking/"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
