from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.BookingsListView.as_view(),
         name='booking_home'),
    path('booking/create', views.CreateBooking.as_view(),
         name='createbooking'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(),
         name='booking-detail')
]
