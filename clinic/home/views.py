from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from authentication.views import login_required
# Create your views here.

@login_required
def home(request):


    return HttpResponse( "HOME")

    