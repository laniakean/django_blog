# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse(f'안녕하세요. {name}님, {age}살 이시군요.') 

#def mysum(request, x=0, y=0, z=0):
    #request : HttpRequest
#    return HttpResponse(int(x) + int(y) + int(z))

# Create your views here.
