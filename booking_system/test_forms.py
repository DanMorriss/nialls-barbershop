from django.test import TestCase
from datetime import datetime, timedelta
from .forms import (BookingForm,
                    SelectHaircutForm,
                    Services,
                    SelectDateForm,
                    SelectTimeForm)


class TestBookingForm(TestCase):

    def test_date_of_booking_is_required(self):
        booking = BookingForm({'date_of_booking': '',
                               'service_name': 'Haircut',
                               'start_time': '09:00:00',
                               'username': 'Testy McTester'})
        self.assertFalse(booking.is_valid())
        self.assertIn('date_of_booking', booking.errors.keys())

    def test_date_cannot_be_in_past(self):
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        booking = SelectDateForm({'date_of_booking': yesterday,
                                  'service_name': 'Haircut',
                                  'start_time': '09:00:00',
                                  'username': 'Testy McTester'})
        self.assertFalse(booking.is_valid())
        self.assertEqual(booking.errors,
                         {'__all__': ['Please select a date in the future.']})

    def test_service_name_is_required(self):
        booking = BookingForm({'date_of_booking': '2024-24-02',
                               'service_name': '',
                               'start_time': '09:00:00',
                               'username': 'Testy McTester'})
        self.assertFalse(booking.is_valid())
        self.assertIn('date_of_booking', booking.errors.keys())

    def test_start_time_is_required(self):
        booking = BookingForm({'date_of_booking': '2024-24-02',
                               'service_name': 'Haircut',
                               'start_time': '',
                               'username': 'Testy McTester'})
        self.assertFalse(booking.is_valid())
        self.assertIn('date_of_booking', booking.errors.keys())

    def test_username_is_required(self):
        booking = BookingForm({'date_of_booking': '2024-24-02',
                               'service_name': 'Haircut',
                               'start_time': '09:00:00',
                               'username': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('date_of_booking', booking.errors.keys())

    def test_fields_are_explicit_in_form_meta_class(self):
        booking = BookingForm()
        self.assertEqual(booking.Meta.fields,
                         ["date_of_booking", "service_name", "start_time"])


class TestSelectHaircutForm(TestCase):

    def test_select_haircut_is_required(self):
        booking = SelectHaircutForm({'service_name': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('service_name', booking.errors.keys())

    def test_list_of_services_is_available(self):
        services_in_database = Services.objects.all()
        form = SelectHaircutForm()
        services_in_form = form.fields['service_name'].queryset
        self.assertQuerysetEqual(services_in_database, services_in_form)


class TestSelectDateForm(TestCase):

    def test_select_date_is_required(self):
        booking = SelectDateForm({'date_of_booking': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('date_of_booking', booking.errors.keys())

    def test_date_cannot_be_in_past(self):
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        booking = SelectDateForm({'date_of_booking': yesterday})
        self.assertFalse(booking.is_valid())
        self.assertEqual(booking.errors,
                         {'__all__': ['Please select a date in the future.']})


class TestSelectTimeForm(TestCase):

    def test_select_time_is_required(self):
        booking = SelectTimeForm({'start_time': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('start_time', booking.errors.keys())
