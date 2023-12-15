from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'catalogodigital.html')

def nicetomeetyou(request):
    return render(request, 'cities/florianopolis/nicetomeetyou.html')

