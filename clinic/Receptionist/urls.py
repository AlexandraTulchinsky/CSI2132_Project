from django.urls import path
from . import views

urlpatterns = [

    path('Add Patient', views.index),
    path('Set Appointment', views.index2),
    path('Edit Patient', views.index3),
    path('menu', views.index4),

]