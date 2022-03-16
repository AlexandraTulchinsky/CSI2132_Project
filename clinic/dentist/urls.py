from django.urls import path
from . import views

urlpatterns = [
    path('', views.dentistHome, name = 'dentistHome'),
    path('view_appt', views.viewAppt, name = 'viewAppointments')
]