from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('catalogodigital', views.index, name='index'),
    path('ajrcutelaria', views.ajrcutelaria, name='ajrcutelaria'),
    path('residencialvivatorres', views.residencialvivatorres, name='residencialvivatorres'),
    
]