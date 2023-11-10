from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.BookingsList.as_view(),
         name='booking_home'),
    path('booking/create', views.CreateBooking.as_view(),
         name='createbooking'),
]
