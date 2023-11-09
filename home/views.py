from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from booking_system.models import Services


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        return context
