from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    response = HttpResponse("Rango says hey there partner!")
    response.write("<br/> <a href='/rango/about/'>About</a>")
    return response
    #return HttpResponse("Rango says hey there partner!")

def about(request):
    response = HttpResponse("Rango says here is the about page.")
    response.write("<br/> <a href='/rango/'>Index</a>")
    return response
    #return HttpResponse("Rango says here is the about page.")
