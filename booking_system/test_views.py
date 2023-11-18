from django.test import TestCase
from .models import User, Booking
from django.urls import reverse


class BaseTest(TestCase):

    def setUp(self):

        self.customer1 = User.objects.create_user(
            username='TestCustomer',
            password='YoullNeverGuessThis')

        self.customer2 = User.objects.create_user(
            username='Testy McTester',
            password='WordyPass1'
        )

        self.admin = User.objects.create_user(
            username='admin',
            password='TheSafestPasswordEver',
            is_superuser=True)

        self.booking1 = Booking.objects.create({
            'date_of_booking': '2040-24-02',
            'service_name': 'Haircut',
            'start_time': '09:00:00',
            'username': 'Testy McTester'})

        self.booking2 = Booking.objects.create({
            'date_of_booking': '2040-12-08',
            'service_name': 'Haircut',
            'start_time': '12:30:00',
            'username': 'TestCustomer'})


class TestBookingsListView(TestCase):

    def test_redirect_to_login_if_not_logged_in(self):
        response = self.client.get('/booking/')
        self.assertRedirects(response, '/accounts/login/?next=%2Fbooking%2F')

    # def test_if_admin_get_all_bookings(self):
    #     self.client.login(username='admin',
    #                       password='TheSafestPasswordEver')
    #     response = self.client.get('/booking/')
    #     self.assertEqual(response.status_code, 200)
