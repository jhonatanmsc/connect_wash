from django.contrib import admin
from django.urls import path

from apps.core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name=HomeView.name)
]
