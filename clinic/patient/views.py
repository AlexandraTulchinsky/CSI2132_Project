from django.shortcuts import render
from django.db import connection 

# Create your views here.
from django.http import HttpResponse

# def dentistHome(request):
#     return render(request,'patientpage.html')

def viewAppt(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Patient" WHERE "Patient"."PatientID" = 101') # WHERE Date > today OR (DATE = today AND Start_time > now)
        apptRows = dictfetchone(cursor) # apptRows is what? an array? can I iterate through it?
    print(apptRows)
    context = {'apptRows': apptRows[0]}
    return render(request, 'patientpage.html', apptRows[0])
    #render(apptRows)

# def index(request):
#     if request.method == "GET":
#         return render (request, "patientpage.html")

#     return HttpResponse()

def dictfetchone(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]