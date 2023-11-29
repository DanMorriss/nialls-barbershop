from django.contrib import admin
from .models import Services, Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Class to view the Bookings in the admin panel"""
    list_display = ('username',
                    'date_of_booking',
                    'service_name',
                    'start_time',
                    'end_time',
                    'confirmed')
    list_filter = ('date_of_booking', 'username')
    search_fields = ['username', 'service_name']
    actions = ['conform_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)


@admin.register(Services)
class BookingServices(admin.ModelAdmin):
    """Class to view the Services in the admin panel"""
    list_display = ('service_name', 'session_length', 'cost')
