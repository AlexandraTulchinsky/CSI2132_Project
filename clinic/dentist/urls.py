from django.urls import path
from . import views

urlpatterns = [
    path('', views.dentistHome, name = 'dentistHome'),
    path('view_appt', views.viewAppt, name = 'viewAppointments'),
    path('view_procedures', views.viewProcedures, name = 'viewProcedures'),
    path('view_patient_records', views.viewRecords, name = 'viewRecords')
]