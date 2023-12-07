from django.test import TestCase
from .models import Booking, Services
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from django.core import mail
from django.urls import reverse

"""
Module: test_views.py
Description: This module contains unit tests for various views in a Django web application related to booking management.

Test classes:
1. SetupTests - Set up initial data for view tests.
2. TestBookingsListView - Tests for the BookingsListView view.
3. TestPastBookingsView - Tests for the PastBookingsView view.
4. EmailTest - Tests for email functionality.
5. TestCreateBookingView - Tests for the CreateBookingView view.
6. TestUpdateBookingView - Tests for the UpdateBookingView view.
7. TestBookingDetailView - Tests for the BookingDetailView view.
8. TestBookingDeleteView - Tests for the BookingDeleteView view.
9. TestConfirmBookingView - Tests for the ConfirmBookingView view.
"""


class SetupTests(TestCase):
    """
    A class to set up initial data for view tests.
    - Create a service
    - Create an admin user
    - Create 2 test users
    - Create 3 bookings
    """
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
    """
    Class: TestBookingsListView
    Description: Contains unit tests for the BookingsListView view.

    Methods:
    - test_redirect_to_login_if_not_logged_in: Test redirection to login if
    not logged in.
    - test_if_admin_gets_all__future_bookings: Test if admin gets all future
    bookings.
    - test_user_is_shown_their_future_bookings: Test if the user is shown
    their future bookings.
    """
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


class TestPastBookingsView(SetupTests):
    """
    Class: TestPastBookingsView
    Description: Contains unit tests for the PastBookingsView view.

    Methods:
    - test_redirect_to_login_if_not_logged_in: Test redirection to login if
    not logged in.
    - test_only_past_bookings_shown: Test only past bookings are shown.
    """
    def test_redirect_to_login_if_not_logged_in(self):
        response = self.client.get('/booking/booking-past')
        self.assertRedirects(response,
                             '/accounts/login/?next=%2Fbooking%2Fbooking-past')

    def test_only_past_bookings_shown(self):
        self.client.login(username='test_user1', password='getmein123')
        response = self.client.get('/booking/booking-past')
        # Check user can view the page
        self.assertEqual(response.status_code, 200)
        # Check only the users bookings are available
        self.assertEqual(len(response.context['object_list']), 1)
        self.assertEqual(response.context['object_list'][0].username.username,
                         'test_user1')
        # Check bookings are in the past
        today = datetime.now()
        for booking in response.context['object_list']:
            self.assertTrue(booking.date_of_booking < today.date())


class EmailTest(TestCase):
    """
    Class: EmailTest
    Description: Contains unit tests for email functionality.

    Methods:
    - test_send_email_confirmation: Test sending email confirmation.
    """
    def test_send_email_confirmation(self):
        subject = 'Subject'
        message = 'Message'
        mail.send_mail(subject, message, 'from@me.com', ['to@you.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, subject)


class TestCreateBookingView(SetupTests):
    """
    Class: TestCreateBookingView
    Description: Contains unit tests for the CreateBookingView view.

    Methods:
    - test_load_booking_form: Test loading the booking form.
    - test_user_must_be_logged_in: Test that the user must be logged in.
    """
    def test_load_booking_form(self):
        self.client.login(username='test_user1', password='getmein123')
        response = self.client.get('/booking/create')
        self.assertEqual(response.status_code, 200)

    def test_user_must_be_logged_in(self):
        response = self.client.get('/booking/create')
        self.assertRedirects(response,
                             '/accounts/login/?next=%2Fbooking%2Fcreate')


class TestUpdateBookingView(SetupTests):
    """
    Class: TestUpdateBookingView
    Description: Contains unit tests for the UpdateBookingView view.

    Methods:
    - test_load_booking_form: Test loading the booking form.
    - test_user_must_be_booking_owner: Test that the user must be the booking
    owner.
    - test_user_must_be_logged_in: Test that the user must be logged in.
    """
    def test_load_booking_form(self):
        self.client.login(username='test_user1', password='getmein123')
        response = self.client.get(reverse('booking-update', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_user_must_be_booking_owner(self):
        self.client.login(username='test_user2', password='getmein123')
        response = self.client.get(reverse('booking-update', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_user_must_be_logged_in(self):
        response = self.client.get(reverse('booking-update', args=[1]))
        self.assertEqual(response.status_code, 302)


class TestBookingDetailView(SetupTests):
    """
    Class: TestBookingDetailView
    Description: Contains unit tests for the BookingDetailView view.

    Methods:
    - test_load_booking_detail: Test loading the booking detail.
    - test_user_must_be_booking_owner: Test that the user must be the booking
    owner.
    - test_user_must_be_logged_in: Test that the user must be logged in.
    """
    def test_load_booking_detail(self):
        self.client.login(username='test_user1', password='getmein123')
        response = self.client.get(reverse('booking-detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_user_must_be_booking_owner(self):
        self.client.login(username='test_user2', password='getmein123')
        response = self.client.get(reverse('booking-detail', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_user_must_be_logged_in(self):
        response = self.client.get(reverse('booking-detail', args=[1]))
        self.assertEqual(response.status_code, 302)


class TestBookingDeleteView(SetupTests):
    """
    Class: TestBookingDeleteView
    Description: Contains unit tests for the BookingDeleteView view.

    Methods:
    - test_user_cant_delete_another_users_booking: Test that the user can't
    delete another user's booking.
    - test_user_can_delete_their_own_booking: Test that the user can delete
    their own booking.
    - test_admin_can_delete_bookings: Test that the admin can delete bookings.
    """
    def test_user_cant_delete_another_users_booking(self):
        self.client.login(username='test_user2', password='getmein123')
        response = self.client.get(reverse('booking-delete', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_user_can_delete_their_own_booking(self):
        self.client.login(username='test_user1', password='getmein123')
        response = self.client.get(reverse('booking-delete', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_admin_can_delete_bookings(self):
        self.client.login(username='admin', password='Superuser123')
        response = self.client.get(reverse('booking-delete', args=[1]))
        self.assertEqual(response.status_code, 200)


class TestConfirmBookingView(SetupTests):
    """
    Class: TestConfirmBookingView
    Description: Contains unit tests for the ConfirmBookingView view.

    Methods:
    - test_admin_can_confirm_booking: Test that the admin can confirm a
    booking.
    - test_users_cant_confirm_bookings: Test that regular users can't confirm
    bookings.
    """
    def test_admin_can_confirm_booking(self):
        self.client.login(username='admin', password='Superuser123')
        response = self.client.get(reverse('confirm-booking', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_users_cant_confirm_bookings(self):
        self.client.login(username='test_user2', password='getmein123')
        response = self.client.get(reverse('confirm-booking', args=[1]))
        self.assertEqual(response.status_code, 302)
