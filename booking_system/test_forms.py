from django.test import TestCase
from datetime import datetime, timedelta
from .forms import BookingForm
from .models import Services, Booking
from django.contrib.auth.models import User


class TestBookingForm(TestCase):

    def setUp(self):
        # Create a test service entry
        self.test_service = Services.objects.create(
            service_name='Test Service',
            session_length=timedelta(hours=0.5),
            cost=20.00,
            description='Test description'
        )
        # Data for a valid booking
        self.common_data = {
            'username': 'Testy McTester',
            'date_of_booking': '2024-02-24',
            'service_name': self.test_service,
            'start_time': '09:00:00',
            'end_time': '09:30:00',
            'confirmed': False,
            'message': '',
            }

    # Create a valid booking
    def create_booking(self, additional_data=None):
        data = self.common_data.copy()
        if additional_data:
            data.update(additional_data)
        return BookingForm(data)

    # Test the setup is working
    def test_the_form_works(self):
        booking = self.create_booking()
        if not booking.is_valid():
            print(booking.errors)
        self.assertTrue(booking.is_valid())

    def test_date_of_booking_is_required(self):
        booking = self.create_booking({'date_of_booking': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('date_of_booking', booking.errors.keys())
        self.assertEqual(booking.errors,
                         {'date_of_booking': ['This field is required.']})

    def test_date_cannot_be_in_past(self):
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        booking = self.create_booking({'date_of_booking': yesterday})
        self.assertFalse(booking.is_valid())
        self.assertEqual(booking.errors,
                         {'__all__': ['Please select a date in the future.']})

    def test_service_name_is_required(self):
        booking = self.create_booking({'service_name': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('service_name', booking.errors.keys())
        self.assertEqual(booking.errors,
                         {'service_name': ['This field is required.']})

    def test_start_time_is_required(self):
        booking = self.create_booking({'start_time': ''})
        self.assertFalse(booking.is_valid())
        self.assertIn('start_time', booking.errors.keys())
        self.assertEqual(booking.errors,
                         {'start_time': ['This field is required.']})

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


class TestBookingSearchForm(TestCase):

    def setUp(self):
        # Create a test service entry
        self.test_service = Services.objects.create(
            service_name='Test Service',
            session_length=timedelta(hours=0.5),
            cost=20.00,
            description='Test description'
        )

        # Create an admin user
        self.admin = User.objects.create_superuser(
            username='admin',
            password='Superuser123'
        )

        # Create test users
        self.test_user1 = User.objects.create_user(
            username='Test User 1',
            password='getmein123'
        )

        self.test_user2 = User.objects.create_user(
            username='Test User 2',
            password='getmein234'
        )

        # Create bookings
        Booking.objects.create(
            username=self.test_user1,
            date_of_booking='2024-02-24',
            service_name=self.test_service,
            start_time='09:00:00',
            end_time='09:30:00',
            confirmed=False,
            message='',
        )

        Booking.objects.create(
            username=self.test_user2,
            date_of_booking='2024-02-26',
            service_name=self.test_service,
            start_time='10:00:00',
            end_time='10:30:00',
            confirmed=False,
            message='Test message.',
        )

    def test_return_all_future_bookings(self):
        self.client.login(username='admin', password='Superuser123')
        response = self.client.get('/booking/')
        # Check admin can view the page
        self.assertEqual(response.status_code, 200)
        # Check both bookings are on the page
        self.assertEqual(len(response.context['object_list']), 2)

    def test_search_by_username(self):
        self.client.login(username='admin', password='Superuser123')
        search_data = {'search_query': 'Test User 1'}
        response = self.client.get('/booking/', data=search_data)
        # Check the page is displaying
        self.assertEqual(response.status_code, 200)
        # Check the list only contains the searched for data
        self.assertEqual(len(response.context['object_list']), 1)
        self.assertEqual(
            response.context['object_list'][0].username.username,
            'Test User 1'
        )

    def test_search_by_date(self):
        self.client.login(username='admin', password='Superuser123')
        search_data = {'selected_date': '2024-02-26'}
        response = self.client.get('/booking/', data=search_data)
        # Check the page is displaying
        self.assertEqual(response.status_code, 200)
        # Check the list only contains the searched for data
        self.assertEqual(len(response.context['object_list']), 1)
        self.assertEqual(
            response.context['object_list'][0].username.username,
            'Test User 2'
        )
