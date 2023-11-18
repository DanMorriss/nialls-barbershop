from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Booking, Services, BOOKING_TIME
from datetime import date
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
    # Without this next line django would look here:
    # <app>/<model>_<viewtype>.html booking_system/booking_list
    template_name = 'booking_system/booking_home.html'
    paginate_by = 25

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Booking.objects.filter(
                date_of_booking__gte=date.today()).order_by(
                    'date_of_booking', 'start_time')
            return queryset
        else:
            return Booking.objects.filter(
                username=self.request.user).filter(
                    date_of_booking__gte=date.today())


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


# class BookingWizardView(LoginRequiredMixin, SessionWizardView):
#     form_list = [SelectHaircutForm, SelectDateForm, SelectTimeForm]
#     template_name = 'booking_system/booking_wizard.html'

#     def form_valid(self, form):
#         form.instance.username = self.request.user
#         form.instance.calculateEndTime()
#         return super().form_valid(form)

#     def done(self, form_list, **kwargs):
#         for form in form_list:
#             print(form.cleaned_data)
#             form.save()

#         return HttpResponseRedirect(reverse('booking-home'))
