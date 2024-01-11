from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajrcutelaria', views.ajrcutelaria, name='ajrcutelaria'),
    path('padrao', views.padrao, name='padrao'),
    
    
]