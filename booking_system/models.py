from django.db import models
from django.contrib.auth.models import User
import datetime

BOOKING_TIME = ((datetime.time(9, 0, 0), '9:00am'),
                (datetime.time(9, 15, 0), '9:15am'),
                (datetime.time(9, 30, 0), '9:30am'),
                (datetime.time(9, 45, 0), '9:45am'),
                (datetime.time(10, 0, 0), '10:00am'),
                (datetime.time(10, 15, 0), '10:15am'),
                (datetime.time(10, 30, 0), '10:30am'),
                (datetime.time(10, 45, 0), '10:45am'),
                (datetime.time(11, 0, 0), '11:00am'),
                (datetime.time(11, 15, 0), '11:15am'),
                (datetime.time(11, 30, 0), '11:30am'),
                (datetime.time(11, 45, 0), '11:45am'),
                (datetime.time(12, 0, 0), '12:00pm'),
                (datetime.time(12, 15, 0), '12:15pm'),
                (datetime.time(12, 30, 0), '12:30pm'),
                (datetime.time(12, 45, 0), '12:45pm'),
                (datetime.time(13, 0, 0), '1:00pm'),
                (datetime.time(13, 15, 0), '1:15pm'),
                (datetime.time(13, 30, 0), '1:30pm'),
                (datetime.time(13, 45, 0), '1:45pm'),
                (datetime.time(14, 0, 0), '2:00pm'),
                (datetime.time(14, 15, 0), '2:15pm'),
                (datetime.time(14, 30, 0), '2:30pm'),
                (datetime.time(14, 45, 0), '2:45pm'),
                (datetime.time(15, 0, 0), '3:00pm'),
                (datetime.time(15, 15, 0), '3:15pm'),
                (datetime.time(15, 30, 0), '3:30pm'),
                (datetime.time(15, 45, 0), '3:45pm'),
                (datetime.time(16, 0, 0), '4:00pm'),
                (datetime.time(16, 15, 0), '4:15pm'),
                (datetime.time(16, 30, 0), '4:30pm'),
                (datetime.time(16, 45, 0), '4:45pm'),
                )


class Services(models.Model):
    """
    Model for the list of haircuts offered.

    Fields:
    service_name(CharField): The name of the haircut or service.
    session_length(DurationField): How long the session lasts.
    cost(DecimalField): The cost of the service to 2 decimal places.

    Methods:
    __str__: Returns the service name
    """
    service_name = models.CharField(max_length=250)
    session_length = models.DurationField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.service_name


class Booking(models.Model):
    """
    Model to create a booking, linked to the user that the booking is for.
    The bookings will be displayed in date and time order,
    with the newest booking first.

    Fields:
    username(ForeignKey): The user the service is for.
    date_of_booking(DateField): The day the haircut is for.
    service_name(ForeignKey): The service booked.
    start_time(TimeField): The start time of the booking.
    end_time(TimeField): The end time of the booking.

    Methods:
    __str__: Returns the booking details.
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_booking = models.DateField()
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE)
    start_time = models.TimeField(choices=BOOKING_TIME)
    end_time = models.TimeField(editable=False, blank=True, null=True)

    class Meta:
        ordering = ['date_of_booking', 'start_time']

    def __str__(self):
        return f"{self.service_name} for {self.username} on {self.date_of_booking} at {self.start_time}"

    def calculateEndTime(self):
        if self.start_time and self.service_name:
            start_datetime = datetime.datetime.combine(self.date_of_booking, self.start_time)
            session_length = self.service_name.session_length
            end_datetime = start_datetime + session_length
            self.end_time = end_datetime.time()
            self.save()
