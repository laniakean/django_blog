# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)


#def mysum(request, x=0, y=0, z=0):
    #request : HttpRequest
#    return HttpResponse(int(x) + int(y) + int(z))

# Create your views here.
