from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nicetomeetyou', views.nicetomeetyou, name='nicetomeetyou'),
    path('ajrcutelaria', views.ajrcutelaria, name='ajrcutelaria'),
    
]