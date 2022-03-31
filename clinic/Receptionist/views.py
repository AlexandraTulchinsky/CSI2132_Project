from datetime import date
import random
from xmlrpc.client import MAXINT
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from authentication.views import login_required

from django.db import models
from django.db.models import Model
from random import randint

# Create your views here.
def index4(request):
    if request.method == "GET":
         return render (request, "menu.html")
   
    return HttpResponse()

def index3(request):

    if request.method == "GET":
        return render (request, "viewEditPatient.html")

    elif request.method == "POST":

        patID = request.POST["patID"]
        SSN = request.POST["SSN"]
        house = request.POST["houseNo"]
        street = request.POST["street"]
        city = request.POST["city"]
        province = request.POST["province"]
        first = request.POST["fName"]
        last = request.POST["lName"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        dob = request.POST["dob"]
        phone = request.POST["phone"]

    if "submit" in request.POST:
        with connection.cursor() as cursor:
            #if any are the fields are left empty, the value from the table is updated instead
            if patID == "":
                messages.info(request, 'Please enter a patient ID!')
                #do nothing 
            else:
                patID = int(patID)
                if SSN == "":
                    cursor.execute('SELECT "SSN_patient" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    SSN = cursor.fetchone()
                if house == "":
                    cursor.execute('SELECT "House_no" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    house = cursor.fetchone() 
                if street == "":
                    cursor.execute('SELECT "Street" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    street = cursor.fetchone()
                if city == "":
                    cursor.execute('SELECT "City_name" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    city = cursor.fetchone()
                if province == "":
                    cursor.execute('SELECT "Province" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    province = cursor.fetchone()
                if first == "":
                    cursor.execute('SELECT "First_name" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    first = cursor.fetchone()
                if last == "":
                    cursor.execute('SELECT "Last_name" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    last = cursor.fetchone()  
                if gender == "":
                    cursor.execute('SELECT "Gender" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    gender = cursor.fetchone()
                if email == "":
                    cursor.execute('SELECT "Email_patient" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    email = cursor.fetchone()
                if dob == "":
                    cursor.execute('SELECT "Dob" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    dob = cursor.fetchone()
                if phone == "":
                    cursor.execute('SELECT "Phone_no_patient" FROM "Patient" WHERE "PatientID" = %s',  [patID])
                    phone = cursor.fetchone()   
                sql = 'Update "Patient" Set "SSN_patient" = %s, "House_no" = %s, "Street" = %s, "City_name" = %s, "Province" = %s, "First_name" = %s, "Last_name" = %s, "Gender" = %s, "Email_patient" = %s, "Dob" = %s, "Phone_no_patient" = %s WHERE "PatientID" = %s'
                val = (SSN,house,street,city,province,first,last,gender,email, dob, phone, patID)
                cursor.execute(sql, val)
            
    return HttpResponse()

def index2(request):

    if request.method == "GET":
        return render (request, "setAppt.html")

    elif request.method == "POST":

        day = request.POST["day"]
        roomNo = request.POST["roomNo"]
        start = request.POST["start"]
        end = request.POST["end"]
        proType = request.POST["proType"]
        state = request.POST["state"]

    if "submit" in request.POST:

        ApptID = random.randint(0,MAXINT)
       
        
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO "Appointment" VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (0,0,0,day,roomNo,start,end,proType,state,ApptID))
    

    return HttpResponse()


def index(request):

    if request.method == "GET":
        return render (request, "addPatient.html")
    

    # if post request comes from the submit button
    # then saving patient info in database

    elif request.method == "POST":

        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        SSN = request.POST["ssn"]
        phone_no = request.POST["phoneNo"]
        gender = request.POST["gender"]
        email = request.POST["email"]
        houseNo = request.POST["houseNo"]
        street = request.POST["street"]
        city = request.POST["city"]
        prov = request.POST["province"]
        dob = request.POST["dob"]


        if "submit" in request.POST:

          
           # SQL = 'abc'

           # while (SQL != ''):

                    id = random.randint(0,MAXINT)
              #  SQL = 'SELECT "PatientID" FROM Patient WHERE PateintID = id '

             #   if (SQL==''):
                    with connection.cursor() as cursor:
                          cursor.execute('INSERT INTO "Patient" VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (id, SSN, houseNo, street, city, prov, first_name, last_name, gender, email, dob, phone_no))
                  #  break

                #else:
                #    continue

       
       # if "back" in request.POST: 
        #    return HttpResponseRedirect(redirect('home.html'))

        

    return HttpResponse()

        





  
  