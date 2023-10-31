from django.db import models
from django.contrib.auth.models import User

BOOKING_TIME = ((1, "9:00am"), (2, "9:15am"), (3, "9:30am"), (4, "9:45am"),
                (5, "10:00am"), (6, "10:15am"), (7, "10:30am"), (8, "10:45am"),
                (9, "11:00am"), (10, "11:15am"), (11, "11:30am"),
                (12, "11:45am"), (13, "12:00pm"), (14, "12:15pm"),
                (15, "12:30pm"), (16, "12:45pm"), (17, "2:00pm"),
                (18, "2:15pm"), (19, "2:30pm"), (20, "2:45pm"),
                (21, "3:00pm"), (22, "3:15pm"), (23, "3:30pm"), (24, "3:45pm"),
                (25, "4:00pm"), (26, "4:15pm"), (27, "4:30pm"), (28, "4:45pm"),
                (25, "4:00pm"), (26, "4:15pm"), (27, "4:30pm"))


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
    start_time = models.TimeField(choices=BOOKING_TIME, default=1)
    end_time = models.TimeField()

    class Meta:
        ordering = ['date_of_booking', 'start_time']

    def __str__(self):
        return f"{self.service_name} for {self.username} on {self.date_of_booking} at {self.start_time}"
