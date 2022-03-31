from django.urls import path
from . import views

urlpatterns = [

    path('patientpage', views.viewPatient),
    path('thankyou', views.thankyou)


]