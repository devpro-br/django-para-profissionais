from django.contrib import admin  # noqa F401
from django.urls import path

from devpro.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
]
