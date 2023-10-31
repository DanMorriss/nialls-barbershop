from django.contrib import admin
from .models import Services, Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Class to view the Bookings in the admin panel"""
    list_display = ('username', 'date_of_booking', 'service_name', 'start_time')
    list_filter = ('date_of_booking',)


@admin.register(Services)
class BookingServices(admin.ModelAdmin):
    """Class to view the Services in the admin pannel"""
    list_display = ('service_name', 'session_length', 'cost')
