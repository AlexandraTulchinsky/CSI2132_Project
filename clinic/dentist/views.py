from django.db import connection
from django.shortcuts import render

def dentistHome(request):
    return render(request, 'dentistHome.html')

def viewAppt(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Branch"') # WHERE Date > today OR (DATE = today AND Start_time > now)
        apptRows = cursor.fetchall() # apptRows is what? an array? can I iterate through it?
    print(apptRows)
    return render(request, 'viewAppointments.html')