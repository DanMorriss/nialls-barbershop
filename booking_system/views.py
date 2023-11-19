from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Booking, Services, BOOKING_TIME
from datetime import date, datetime
from .forms import (BookingForm,
                    # SelectHaircut,
                    SelectHaircutForm,
                    SelectDateForm,
                    SelectTimeForm)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy, reverse
from formtools.wizard.views import SessionWizardView
from django.core.exceptions import PermissionDenied


class BookingsListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_system/booking_home.html'
    paginate_by = 25

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Booking.objects.filter(
                date_of_booking__gte=timezone.now().date(),
                start_time__gte=timezone.now()
                ).order_by('date_of_booking', 'start_time')
        else:
            queryset = Booking.objects.filter(
                date_of_booking__gte=timezone.now().date(),
                start_time__gte=timezone.now()
                ).order_by('date_of_booking', 'start_time')
        return queryset


class CreateBookingView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'booking_system/booking_form.html'
    success_url = reverse_lazy('booking-home')
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.calculateEndTime()
        return super().form_valid(form)


class UpdateBookingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    template_name = 'booking_system/booking_form.html'
    success_url = reverse_lazy('booking-home')
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.calculateEndTime()
        return super().form_valid(form)

    def test_func(self):
        booking = self.get_object()
        return (self.request.user == booking.username or
                self.request.user.is_superuser)


class BookingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Booking
    # <app>/<model>_<viewtype>.html booking_system/booking_detail.html

    def test_func(self):
        booking = self.get_object()
        return (self.request.user == booking.username or
                self.request.user.is_superuser)


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking-home')

    def test_func(self):
        booking = self.get_object()
        return (self.request.user == booking.username or
                self.request.user.is_superuser)


class BookingWizardView(LoginRequiredMixin, SessionWizardView):
    form_list = [SelectHaircutForm, SelectDateForm, SelectTimeForm]
    template_name = 'booking_system/booking_wizard.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.date_of_booking = form.cleaned_data.get('date_of_booking')
        form.instance.calculateEndTime()
        return super().form_valid(form)

    def done(self, form_list, **kwargs):
        # Extract data from the forms
        service_name = form_list[0].cleaned_data.get('service_name')
        date_of_booking = form_list[1].cleaned_data.get('date_of_booking')
        start_time = form_list[2].cleaned_data.get('start_time')

        # Create a new Booking instance
        booking = Booking(
            username=self.request.user,
            date_of_booking=date_of_booking,
            service_name=service_name,
            start_time=start_time,
            confirmed=False
        )

        # Calculate and set the end time
        start_datetime = datetime.combine(date_of_booking, start_time)
        session_length = service_name.session_length
        end_datetime = start_datetime + session_length
        booking.end_time = end_datetime.time()

        booking.save()

        return HttpResponseRedirect(reverse('booking-home'))
