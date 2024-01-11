from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cities/florianopolis/catalogodigital/catalogodigital.html')

def ajrcutelaria(request):
    return render(request, 'cities/sapiranga/ajrcutelaria/ajrcutelaria.html')

