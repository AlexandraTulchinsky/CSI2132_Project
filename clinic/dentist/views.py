from django.db import connection
from django.shortcuts import render

def dentistHome(request):
    return render(request, 'dentistHome.html')

def viewAppt(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Appointment" WHERE "Status" = \'upcoming\'')
        apptRows = dictfetchone(cursor)

    context = {'apptRows': apptRows}
    return render(request, 'viewAppointments.html', context)

def viewProcedures(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Treatment"')
        treatmentRows = dictfetchone(cursor)

        cursor.execute('SELECT * FROM "Procedure"')
        procedureRows = dictfetchone(cursor)

    context = {'treatmentRows': treatmentRows, 
               'procedureRows': procedureRows}
               
    return render(request, 'viewProcedures.html', context)

def viewRecords(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Record"')
        recordRows = dictfetchone(cursor)

    context = {'recordRows': recordRows}
    return render(request, 'viewRecords.html', context)

def dictfetchone(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]