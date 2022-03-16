from django.db import connection
from django.shortcuts import render

def dentistHome(request):
    return ""

def viewAppt(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "Appointment"') # WHERE Date > today OR (DATE = today AND Start_time > now)
    apptRows = cursor.fetchall()
    return render(request, 'viewAppointments.html')