from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def home(request):

    # this is used to hold all the data in a dictionary

    return render(request, 'bookApp/home.html')
