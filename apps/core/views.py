from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    name = 'home'
    template_name = 'index.html'
