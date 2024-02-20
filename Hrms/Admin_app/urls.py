from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_co/',views.admin_co,name='admin_co'),
]