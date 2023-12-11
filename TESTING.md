# Testing

## Unit Testing

Automated unit tests have been written and used, they can all be found in the following locations:
 - booking_system > test_forms.py
 - booking_system > test_views.py
 - home > test_views.py

### TestBookingForm

The following tests have been written for the BookingForm class:
- test_the_form_works: Test the setup and basic functionality of the form.
- test_date_of_booking_is_required: Test that the date of booking is a required field.
- test_date_cannot_be_in_past: Test that the date of booking cannot be in the past.
- test_service_name_is_required: Test that the service name is a required field.
- test_start_time_is_required: Test that the start time is a required field.
- test_start_time_cannot_be_in_the_past: Test that the start time cannot be in the past.
- test_fields_are_explicit_in_form_meta_class: Test that form fields are explicitly defined in the Meta class.

### TestBookingSearchForm

The following tests have been written for the BookingSearchForm class.
- test_return_all_future_bookings: Test returning all future bookings.
- test_search_by_username: Test searching bookings by username.
- test_search_by_date: Test searching bookings by date.

### TestBookingsListView

The following tests have been written for the BookingsListView view.
- test_redirect_to_login_if_not_logged_in: Test redirection to login if not logged in.
- test_if_admin_gets_all__future_bookings: Test if admin gets all future bookings.
- test_user_is_shown_their_future_bookings: Test if the user is shown their future bookings.

### TestPastBookingsView

The following tests have been written for the PastBookingsView view.
- test_redirect_to_login_if_not_logged_in: Test redirection to login if not logged in.
- test_only_past_bookings_shown: Test only past bookings are shown.

### EmailTest
The following tests have been written for the email functionality.
- test_send_email_confirmation: Test sending email confirmation.

### TestCreateBookingView
The following tests have been written for the CreateBookingView view.
- test_load_booking_form: Test loading the booking form.
- test_user_must_be_logged_in: Test that the user must be logged in.

### TestUpdateBookingView
The following tests have been written for the UpdateBookingView view.
- test_load_booking_form: Test loading the booking form.
- test_user_must_be_booking_owner: Test that the user must be the booking owner.
- test_user_must_be_logged_in: Test that the user must be logged in.

### TestBookingDetailView
The following tests have been written for the BookingDetailView view.
- test_load_booking_detail: Test loading the booking detail.
- test_user_must_be_booking_owner: Test that the user must be the booking owner.
- test_user_must_be_logged_in: Test that the user must be logged in.

### TestBookingDeleteView
The following tests have been written for the BookingDeleteView view.
- test_user_cant_delete_another_users_booking: Test that the user can't delete another user's booking.
- test_user_can_delete_their_own_booking: Test that the user can delete their own booking.
- test_admin_can_delete_bookings: Test that the admin can delete bookings.

### TestConfirmBookingView
The following tests have been written for the ConfirmBookingView view.
- test_admin_can_confirm_booking: Test that the admin can confirm a booking.
- test_users_cant_confirm_bookings: Test that regular users can't confirm bookings.

## Manual Testing

### User: Sign Up

Description:
- A user can sign up by accessing the sign-up form and entering their details.

Steps:
1. Go to the register page
2. Enter the requested details
3. Click Sign Up

Expected: 

- Email should be optional, but if entered a confirmation email should be received by the user
- A username should be unique
- A password should comply with the regulations
- Send to account home upon successful sign-up

Actual:
- As expected, error messages displayed when incorrect or invalid data entered, confirmation email received and redirected to account home.

### User: Login 

Description:
- A user can login with their account details and be redirected to the account home page, unless the "book a haircut" button as clicked prior to login; in that case the user should be directed to the booking form.
- Upon successful login a success message should be displayed to the user.

Steps:
1. Go to the login page
2. Enter username or email and password
3. Click 'Sign In'

Expected:
- The user is directed to the account home page
- A success message is displayed at the top of the screen saying "Successfully signed in as `username`

Actual:
- As expected

### User: Logout

Description:
- The user can logout successfully.

Steps:
1. Click the 'Logout' button from the navbar
2. Click 'Sign Out'

Expected:
- The user is logged out and redirected to the landing page
- A message is displayed saying "You have signed out"

Actual:
- As expected

### User: Book a Haircut

Description:
- A logged in user can book a haircut

Steps:
1. Click a "book a haircut" button or select it from the navbar
2. Select a date from the date picker
3. Select a haircut from the dropdown menu
4. Select a time from the dropdown menu
5. Add a message (optional)
6. Click 'Book'

Expected:
- If a past date is selected an error message is shown saying 'Please select a date in the future'
- If a time in the past is shown an error message is shown saying 'Please select a time in the future'
- The user is redirected to the account home page
- The booking is displayed with the 'Not yet confirmed' message on the upcoming bookings section
- An email confirmation is sent to the user (if they have an email address associated with their account)

Actual:
- As expected


### User: View Upcoming Bookings

Description:
- The user can view all their upcoming bookings

Steps:
- Go to the My Account page from the navbar
- See the bookings in the Upcoming Bookings section

Expected:
- All future bookings are displayed including:
    - Date
    - Service name
    - Time
    - Message icon (if a message is attached to the booking)
    - Confirmation status

Actual:
- As expected

### User: View Past Bookings

Description:
- A user can view their past bookings

Steps:
- From the My Account page click on the 'past bookings' button
- View all past bookings

Expected:
- All past bookings are displayed including:
    - Date
    - Service name
    - Time
    - Message icon (if a message is attached to the booking)
- If more than 25 bookings have been made page pagination will be on display
    - Next >>
    - << Prev

Actual:
- As expected

### User: View Booking Details

Description:
- A user can view the details of a booking

Steps:
- From the My Account page click on a booking card
- View the booking details

Expected:
- Details of the bookins will be shown:
    - Date
    - Service
    - Start time
    - End time
    - Message (if there is one)
    - Confirmation status
- Modification buttons will be available for the user to:
    - Edit Appointment
    - Cancel Appointment

Actual:
- As expected

### User: Update Booking

Description:
- A user can update their booking

Steps:
1. Click on 'Edit Appointment' from the booking detail page
2. Update the booking details

Expected:
- The user cannot someone elses appointment
- The user is taken a pre-populated booking from containing the boooking information
- The user changes any of the information with the same stipulations as when creating a new booking
- The user is redirected to the account home page
- A success message is shown to the user
- A confirmation email is sent to the user (if they have an email address attached to their account)
- The status is reset to 'not yet confirmed'

Actual:
- As expected

### User: Delete Booking

Description:
- A user can delete their booking

Steps:
1. Select 'Cancel Appointment' from the booking detail page
2. Select 'Yes, delete my booking'

Expected:
- The user is redirected to the account home page
- A message saying 'Your booking has been successfully deleted' is displayed to the user
- A confirmation email is sent to the user (if they have an email address attached to their account)

Actual:
- As expected

### User: Update Email

Description:
- A user can update the email address associated with their account.

Steps:
- Click 'Update Email' from the Account section of the Account home page
- Add a (new) email address in the add email field
- Click 'Add email'
- Check your inbox
- Follow the verification link in the email
- Click 'confirm'
- Go back to the 'Update email' page
- Select the (new) email address
- Click 'make primary'

Expected:
- A success message to be shown when email confirmed

Actual:
- As expected

### User: Change Password

Description:
- A user can up update the password associated with their account

Steps:
- Click 'Change Password' from the Account section of the Account home page
- Type your current password
- Type a new password 
- Type the new password again
- Click 'Change password'

Expected:
- A message saying 'Password successfully changed.' is displayed to the user

Actual:
- As expected

### Admin: View Upcoming Bookings

Description:
- An admin user can view all upcoming bookings

Steps:
1. Go to the My Account page
2. View all the upcoming bookings

Expected:
- All bookings are in the future and include:
    - Date
    - Service name
    - Time
    - User
    - Message icon (if a message is attached to the booking)
    - Confirmation status
- If more than 25 bookings have been made page pagination will be on display
    - Next >>
    - << Prev

Actual:
- As expected

### Admin: View Past Bookings

Description:
- An admin user can view all past bookings

Steps:
1. Go to the My Account page
2. Click 'Past Bookings'
3. View all the past bookings

Expected:
- All bookings are in the past and include:
    - Date
    - Service name
    - Time
    - User
    - Message (if a message is attached to the booking)
- If more than 25 bookings have been made page pagination will be on display
    - Next >>
    - << Prev

### Admin: Confirm Booking

Description:
- An admin can confirm a booking for a user

Steps:
1. Click on a booking card with a confirmation status of 'Not yet confirmed' from the admin account home
2. Click 'Confirm Booking'

Expected:
- The admin will be redirected to account home
- A success message will be displayed
- The booking status changes to 'Booking Confirmed'
- A confirmation email will be send to the user (if an email address is associated with the account)

Actual:
- As expected

### Admin: Search by date

Description:
- Admin users can search upcoming bookings by date

Steps:
1. On the account home page in the search bookings section select a date from the date picker
2. Click 'search'

Expected:
- The bookings on the selected date will be displayed
- If no bookings are on the selected date 'No upcoming bookings' will be displayed

Actual:
- As expected

### Admin: Search by Username

Description:
- Admin users can search upcoming bookings by username

Steps:
1. On the account home page in the search bookings section type a username (or part of a username)
2. Click 'search'

Expected:
- The bookings for the user(s) with the entered username will be displayed
- If no bookings are found 'No upcoming bookings' will be displayed

Actual:
- As expected

## Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

![Wave Testing](media/wave-validation.png)

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
- Color contrasts meet a minimum ratio as specified in [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All not textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.1 Coding best practices being followed

## Validator Testing

All pages were run through the [w3 HTML Validator](https://validator.w3.org/).

The Django templating language would not allow the files to be pasted into the validator and as some of the pages were restricted due to login or admin access I used the Chrome DevTools to copy the HTML content and paste that into the validator.

![HTML Validator](media/html-validation.png)

All pages were run through the [Code Institute Pylint](https://pep8ci.herokuapp.com/) validator to ensure all code was pep8 compliant.

![PEP8](media/python-validation.png)

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator.

![JS validator](media/js-validation.png)

This had warnings about the use of let, but as this code came from the Code Institute walkthrough project I assumed it acceptable.

## Lighthouse Reports
All lighthouse reports for all pages came back with a score of at least 91, you can see the full reports below.

Landing Page<br>
![Lighthouse Landing Page](media/lighthouse-landing.png)
Account Home<br>
![Lighthouse Account Home](media/lighthouse-account-home.png)
Booking Detail<br>
![Lighthouse Booking Detail](media/lighthouse-booking-detail.png)
Booking Form<br>
![Lighthouse Booking Form](media/lighthouse-booking-form.png)
Logout<br>
![Lighthouse Logout](media/lighthouse-logout.png)
Sign Up<br>
![Lighthouse Sign Up](media/lighthouse-signup.png)
Log In<br>
![Lighthouse Log In](media/lighthouse-login.png)

## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Firefox and Safari.

Steps to test:

- Open browser and navigate to [Niall's Barbershop](https://niallsbarbershop-e4e7dc2878db.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Click and drag the responsive window slowly to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.
