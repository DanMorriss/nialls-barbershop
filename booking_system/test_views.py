from django.test import TestCase
from .models import Booking, Services
from django.contrib.auth.models import User
from datetime import timedelta, datetime


class SetupTests(TestCase):

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
            username='test_user1',
            password='getmein123'
        )

        self.test_user2 = User.objects.create_user(
            username='test_user2',
            password='getmein234'
        )

        # Create bookings
        Booking.objects.create(
            username=self.test_user1,
            date_of_booking='2023-08-24',
            service_name=self.test_service,
            start_time='09:00:00',
            end_time='09:30:00',
            confirmed=False,
            message='',
        )

        Booking.objects.create(
            username=self.test_user1,
            date_of_booking='2025-08-24',
            service_name=self.test_service,
            start_time='09:00:00',
            end_time='09:30:00',
            confirmed=False,
            message='',
        )

        Booking.objects.create(
            username=self.test_user2,
            date_of_booking='2024-08-24',
            service_name=self.test_service,
            start_time='10:00:00',
            end_time='10:30:00',
            confirmed=False,
            message='Test message.',
        )


class TestBookingsListView(SetupTests):

    def test_redirect_to_login_if_not_logged_in(self):
        response = self.client.get('/booking/')
        self.assertRedirects(response, '/accounts/login/?next=%2Fbooking%2F')

    def test_if_admin_gets_all__future_bookings(self):
        self.client.login(username='admin', password='Superuser123')
        response = self.client.get('/booking/')
        # Check admin can view the page
        self.assertEqual(response.status_code, 200)
        # Check only the future booking is on the page
        self.assertEqual(len(response.context['object_list']), 2)
        self.assertEqual(response.context['object_list'][0].username.username,
                         'test_user2')

    def test_user_is_shown_their_future_bookings(self):
        self.client.login(username='test_user1', password='getmein123')
        response = self.client.get('/booking/')
        # Check user can view the page
        self.assertEqual(response.status_code, 200)
        # Check only their bookings are on the page
        for booking in response.context['object_list']:
            self.assertEqual(booking.username.username, 'test_user1')
        # Check bookings are in the future
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        for booking in response.context['object_list']:
            self.assertTrue(booking.date_of_booking > yesterday.date())
