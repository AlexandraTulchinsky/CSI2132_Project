from datetime import date
import random
from xmlrpc.client import MAXINT
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from authentication.views import login_required

from django.db import models
from django.db.models import Model
from random import randint

# Create your views here.
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

        





  
  