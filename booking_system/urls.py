from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingsList.as_view(), name='account_home')
]
