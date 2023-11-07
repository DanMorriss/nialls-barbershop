from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingsList.as_view(), name='account_home'),
    path('createbooking/', views.CreateBookingView.as_view(), name='create_booking')
]
