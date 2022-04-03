from django.db import connection
from django.shortcuts import render
from authentication.views import login_required

@login_required
def dentistHome(request):
    return render(request, 'dentistHome.html')

@login_required
def viewAppt(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Appointment" WHERE "Status" = \'upcoming\'')
        apptRows = dictfetchone(cursor)

    context = {'apptRows': apptRows}
    return render(request, 'viewAppointments.html', context)

@login_required
def viewProcedures(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Treatment"')
        treatmentRows = dictfetchone(cursor)

        cursor.execute('SELECT * FROM "Procedure"')
        procedureRows = dictfetchone(cursor)

    context = {'treatmentRows': treatmentRows, 
               'procedureRows': procedureRows}
               
    return render(request, 'viewProcedures.html', context)

@login_required
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