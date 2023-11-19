from django.db import models
from django.contrib.auth.models import User
import datetime

BOOKING_TIME = ((datetime.time(9, 0, 0), '9:00am'),
                (datetime.time(9, 30, 0), '9:30am'),
                (datetime.time(10, 0, 0), '10:00am'),
                (datetime.time(10, 30, 0), '10:30am'),
                (datetime.time(11, 0, 0), '11:00am'),
                (datetime.time(11, 30, 0), '11:30am'),
                (datetime.time(12, 0, 0), '12:00pm'),
                (datetime.time(12, 30, 0), '12:30pm'),
                (datetime.time(13, 0, 0), '1:00pm'),
                (datetime.time(13, 30, 0), '1:30pm'),
                (datetime.time(14, 0, 0), '2:00pm'),
                (datetime.time(14, 30, 0), '2:30pm'),
                (datetime.time(15, 0, 0), '3:00pm'),
                (datetime.time(15, 30, 0), '3:30pm'),
                (datetime.time(16, 0, 0), '4:00pm'),
                (datetime.time(16, 30, 0), '4:30pm'),
                )


class Services(models.Model):
    """
    Model for services offered.

    Fields:
        - `service_name` (CharField): The name of the service.
        - `session_length` (DurationField): The duration of the service.
        - `cost` (DecimalField): The cost of the service.

    Methods:
        - `__str__`: Human-readable string representation of the service.

    Attributes:
        - `max_length`: Maximum length for the `service_name` field.

    Returns:
        str: A string representing the name of the service.
    """
    service_name = models.CharField(max_length=250)
    session_length = models.DurationField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.service_name


class Booking(models.Model):
    """
    Model for bookings.

    Fields:
        - `username` (ForeignKey): Reference to the user making the booking.
        - `date_of_booking` (DateField): Date of the reservation.
        - `service_name` (ForeignKey): Reference to the booked service.
        - `start_time` (TimeField): Start time of the reservation chosen from
        predefined choices.
        - `end_time` (TimeField): End time of the reservation, calculated
        based on the start time and service session length.
        - `confirmed` (BooleanField): Indicates whether the booking is
        confirmed.

    Meta:
        - `ordering`: Default ordering for queries based on date and
        start time.

    Methods:
        - `__str__`: Human-readable string representation of the booking.
        - `calculateEndTime`: Calculates and sets the end time based on the
        start time and service session length.
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='username_booking')
    date_of_booking = models.DateField()
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE,
                                     related_name='service_name_booking')
    start_time = models.TimeField(choices=BOOKING_TIME)
    end_time = models.TimeField(editable=False, blank=True, null=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_of_booking', 'start_time']

    def __str__(self):
        return (f"{self.service_name} for {self.username} "
                f"on {self.date_of_booking} at {self.start_time}")

    def calculateEndTime(self):
        if self.start_time and self.service_name:
            start_datetime = datetime.datetime.combine(self.date_of_booking,
                                                       self.start_time)
            session_length = self.service_name.session_length
            end_datetime = start_datetime + session_length
            self.end_time = end_datetime.time()
            self.save()
