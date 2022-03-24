from django.urls import path
from . import views

urlpatterns = [

    path('Add Patient', views.index),
    path('Set Appointment', views.index2)


]