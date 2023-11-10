from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.BookingsList.as_view(),
         name='booking_home'),
]
