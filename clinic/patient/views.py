from django.shortcuts import render
from django.db import connection 
from datetime import date
from datetime import datetime
# Create your views here.
from django.http import HttpResponse

def thankyou(request):
    return render(request,'thankyou.html')


def viewPatient(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Patient" WHERE "Patient"."PatientID" = 101') 
        patientRows = dictfetchone(cursor) 
    #print(apptRows)

    context = {'patientRows': patientRows[0], 'apptRows':viewAppointments(), 'dentistRow':viewTodayAppoint(), 'recRows':viewPatientRecords}
    
    return render(request, 'patientpage.html', context)
    #render(apptRows)

def viewAppointments():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Appointment" WHERE "Status" = \'upcoming\' AND "PatientID" = 101') 
        
        apptRows = dictfetchone(cursor)
    #print(apptRows)

    context = {'apptRows': apptRows}
    return apptRows
    #return render(request, 'patientpage.html', context)

def viewTodayAppoint():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Appointment","Employee" WHERE "Appointment"."Date" = CURRENT_DATE AND "Appointment"."PatientID" = 0 AND "Appointment"."EID" IN (SELECT "EID" FROM "Employee")')
        dentistRow = dictfetchone(cursor)
        print(dentistRow)
        return dentistRow[1]

def viewPatientRecords():
    with connection.cursor() as cursor: 
        cursor.execute('SELECT * FROM "Record" WHERE "Record"."PatientID"= 101')
        recRows = dictfetchone(cursor)

    
    return recRows


def dictfetchone(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]