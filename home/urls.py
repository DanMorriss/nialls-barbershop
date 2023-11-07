from django.urls import path
from home.views import HomeView
from home import views

urlpatterns = [
    path('', views.HomeView.as_view(),
         name='home'),
]
