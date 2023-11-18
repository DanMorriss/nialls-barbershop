from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.BookingsListView.as_view(),
         name='booking-home'),
    path('booking/create', views.CreateBookingView.as_view(),
         name='booking-create'),  # original booking form
    path('booking/<int:pk>/', views.BookingDetailView.as_view(),
         name='booking-detail'),
    path('booking/<int:pk>/update/', views.UpdateBookingView.as_view(),
         name='booking-update'),
    path('booking/<int:pk>/delete/', views.BookingDeleteView.as_view(),
         name='booking-delete'),
    path('booking/booking-wizard/', views.BookingWizardView.as_view(
        [views.SelectHaircutForm, views.SelectDateForm, views.SelectTimeForm]), name='booking-wizard'),
]
