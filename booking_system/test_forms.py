from django.test import TestCase
from datetime import datetime, timedelta
from .forms import BookingForm


class TestBookingForm(TestCase):

    def setUp(self):
        self.common_data = {
            'date_of_booking': '2024-02-24',
            'service_name': 'Haircut',
            'start_time': '09:00:00',
            'message': '',
            }

    def create_booking(self, additional_data=None):
        data = self.common_data.copy()
        if additional_data:
            data.update(additional_data)
        return BookingForm(data)

    def test_date_of_booking_is_required(self):
        booking = self.create_booking({'date_of_booking': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('date_of_booking', booking.errors.keys())

    def test_date_cannot_be_in_past(self):
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        booking = self.create_booking({'date_of_booking': yesterday})
        self.assertFalse(booking.is_valid())

    def test_service_name_is_required(self):
        booking = self.create_booking({'service_name': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('service_name', booking.errors.keys())

    def test_start_time_is_required(self):
        booking = self.create_booking({'start_time': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('start_time', booking.errors.keys())

    def test_start_time_cannot_be_in_the_past(self):
        now = datetime.now()
        an_hour_ago = now - timedelta(hours=1)
        booking = self.create_booking({'start_time': an_hour_ago})
        self.assertFalse(booking.is_valid())

    def test_fields_are_explicit_in_form_meta_class(self):
        booking = BookingForm()
        self.assertEqual(booking.Meta.fields,
                         ["date_of_booking",
                          "service_name",
                          "start_time",
                          "message"])
