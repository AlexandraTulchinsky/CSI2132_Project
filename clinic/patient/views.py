from django.shortcuts import render
from django.db import connection 

# Create your views here.
from django.http import HttpResponse

# def dentistHome(request):
#     return render(request,'patientpage.html')


def viewPatient(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Patient" WHERE "Patient"."PatientID" = 101') 
        patientRows = dictfetchone(cursor) 
    #print(apptRows)
    context = {'patientRows': patientRows[0], 'apptRows':viewAppointments()}
    
    return render(request, 'patientpage.html', context)
    #render(apptRows)

def viewAppointments():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Appointment" WHERE "Status" = \'upcoming\' AND "PatientID" = 101') 
        
        apptRows = dictfetchone(cursor)
    print(apptRows)

    context = {'apptRows': apptRows}
    return apptRows
    #return render(request, 'patientpage.html', context)


def dictfetchone(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]