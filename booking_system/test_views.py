from django.test import TestCase
from .models import Booking, Services
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from django.core import mail
from django.urls import reverse


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


class TestPastBookingsView(SetupTests):
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
    def test_send_email_confirmation(self):
        subject = 'Subject'
        message = 'Message'
        mail.send_mail(subject, message, 'from@me.com', ['to@you.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, subject)


class TestCreateBookingView(SetupTests):
    def test_load_booking_form(self):
        self.client.login(username='test_user1', password='getmein123')
        response = self.client.get('/booking/create')
        self.assertEqual(response.status_code, 200)

    def test_user_must_be_logged_in(self):
        response = self.client.get('/booking/create')
        self.assertRedirects(response,
                             '/accounts/login/?next=%2Fbooking%2Fcreate')


class TestUpdateBookingView(SetupTests):
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
