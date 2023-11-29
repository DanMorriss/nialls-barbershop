from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from formtools.wizard.views import SessionWizardView
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from .models import Booking
from .forms import (BookingForm,
                    SelectHaircutForm,
                    SelectDateForm,
                    SelectTimeForm)
from datetime import date, datetime
import time


class BookingsListView(LoginRequiredMixin, ListView):
    """
    ListView for displaying a paginated list of bookings on booking-home page.

    Attributes:
        - model: Booking from models.py
        - template_name: The path to the template for rendering the view.
        - paginate_by: The number of bookings to display per page.

    Methods:
        - get_queryset(): Retrieves the queryset of bookings to be displayed,
        and filters out past bookings.
        Superusers see all bookings, regular users only see their own bookings.

    Usage:
        - This view displays a paginated list of bookings.
        - If the user is a superuser, the view shows all future bookings.
        - Otherwise, it displays future bookings for the authenticated user.

    Returns:
        - QuerySet: A filtered and ordered QuerySet of bookings to be displayed
        on the template.
    """
    model = Booking
    template_name = 'booking_system/booking_home.html'
    paginate_by = 25

    def get_queryset(self):
        current_date = date.today()
        current_time = time.strftime("%H:%M:%S", time.gmtime())
        if self.request.user.is_superuser:
            queryset = Booking.objects.filter(
                Q(date_of_booking__gt=current_date) |
                Q(date_of_booking=current_date, start_time__gte=current_time)
            ).order_by('date_of_booking', 'start_time')
        else:
            queryset = Booking.objects.filter(
                username=self.request.user).filter(
                    Q(date_of_booking__gt=current_date) |
                    Q(date_of_booking=current_date,
                      start_time__gte=current_time)
                ).order_by('date_of_booking', 'start_time')
        return queryset


class PastBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_system/booking_past.html'
    paginate_by = 25

    def get_queryset(self):
        current_date = date.today()
        current_time = time.strftime("%H:%M:%S", time.gmtime())
        if self.request.user.is_superuser:
            queryset = Booking.objects.filter(
                Q(date_of_booking__lt=current_date) |
                Q(date_of_booking=current_date, start_time__lte=current_time)
            ).order_by('date_of_booking', 'start_time')
        else:
            queryset = Booking.objects.filter(
                username=self.request.user).filter(
                    Q(date_of_booking__lt=current_date) |
                    Q(date_of_booking=current_date,
                      start_time__lte=current_time)
                ).order_by('date_of_booking', 'start_time')
        return queryset


def send_email_confirmation(user, subject, message):
    from_email = 'danielmorriss1@gmail.com'
    to_email = [user.email]

    send_mail(subject, message, from_email, to_email, fail_silently=False)


class CreateBookingView(LoginRequiredMixin, CreateView):
    """
    View for creating a new booking.

    Attributes:
        - model: Booking from models.py
        - template_name: The path to the template for rendering the view.
        - success_url: Redirects to booking-home after a successful form.
        - form_class: The form class to use for creating a new booking.

    Methods:
        - form_valid(form): Overrides the form_valid method.
        Sets the username and calculates the end time
        and sends a confirmation email
        and alerts the user of a successful booking.
    """
    model = Booking
    template_name = 'booking_system/booking_form.html'
    success_url = reverse_lazy('booking-home')
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.calculateEndTime()

        if self.request.user.email:
            service = form.instance.service_name
            date = form.instance.date_of_booking
            time = form.instance.start_time
            email_subject = 'Booking Confirmed'
            email_message = (f'{form.instance.username},\n\n'
                             f'Your {service} on {date} '
                             f'at {time} has been booked!\n\n'
                             f'Comments: {form.instance.message}\n\n'
                             f'Looking forward to seeing you then.'
                             )
            send_email_confirmation(self.request.user,
                                    email_subject,
                                    email_message)

        messages.success(
            self.request,
            "Your booking has been made successfully!",
            extra_tags="alert alert-success alert-dismissible",
        )

        return super().form_valid(form)


class UpdateBookingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for updating an existing booking.

    Attributes:
        - model: Booking from models.py
        - template_name: The path to the template for rendering the view.
        - success_url: Redirect to booking-home after a successful form.
        - form_class: The form class to use for updating a booking.

    Methods:
        - form_valid(form): Overrides the form_valid method for customization.
        Calculates the end time after a successful form submission and sends a 
        confirmation email to the user.

        - test_func(): Checks if the current user is allowed to update the
        booking.
        Users that created the booking and admins have the ability to update.
    """
    model = Booking
    template_name = 'booking_system/booking_form.html'
    success_url = reverse_lazy('booking-home')
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.calculateEndTime()

        if self.request.user.email:
            service = form.instance.service_name
            date = form.instance.date_of_booking
            time = form.instance.start_time
            email_subject = 'Booking Updated'
            email_message = (f'{form.instance.username},\n\n'
                             f'Your {service} on {date} '
                             f'at {time} has been updated!\n\n'
                             f'Comments: {form.instance.message}\n\n'
                             f'Looking forward to seeing you then.'
                             )
            send_email_confirmation(self.request.user,
                                    email_subject,
                                    email_message)

        messages.success(
            self.request,
            "Your booking has been successfully updated!",
            extra_tags="alert alert-success alert-dismissible",
        )

        return super().form_valid(form)

    def test_func(self):
        booking = self.get_object()
        return (self.request.user == booking.username or
                self.request.user.is_superuser)


class BookingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    View for displaying details of a booking.

    Attributes:
        - model: Booking from models.py
        - No template name as the Django default path was used for naming.
        <app>/<model>_<viewtype>.html : booking_system/booking_detail.html

    Methods:
        - test_func(): Checks if the current user is allowed to view the
        booking details. Users that created the booking and admins have access.

    Returns:
        Rendered template with booking details.
    """
    model = Booking

    def test_func(self):
        booking = self.get_object()
        return (self.request.user == booking.username or
                self.request.user.is_superuser)


class BookingDeleteView(DeleteView):
    """
    View for deleting an existing booking.

    Attributes:
        - model: Booking from models.py
        - success_url: Redirect to booking-home after a successful deletion.

    Methods:
        - test_func(): Checks if the current user is allowed to delete
        the booking. Users that created the booking and admins have access.
        The user is shown a success message once the booking has been deleted.
    """
    model = Booking
    success_url = reverse_lazy('booking-home')

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            "Your booking has been successfully deleted!",
            extra_tags="alert alert-danger alert-dismissible",
        )
        return super().delete(request, *args, **kwargs)

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
