from django.db import connection
from django.shortcuts import render

def dentistHome(request):
    return render(request, 'dentistHome.html')

def viewAppt(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Appointment" WHERE "Status" = \'upcoming\'')
        apptRows = dictfetchone(cursor)

    # print(apptRows[1][9]) # test print
    # print(apptRows) # test print

    context = {'apptRows': apptRows}
    return render(request, 'viewAppointments.html', context)

def dictfetchone(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]