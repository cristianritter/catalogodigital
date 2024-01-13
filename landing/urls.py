from django.urls import path
from .views import CatalogoDigital, AJRCutelaria

urlpatterns = [
    path('catalogodigital', CatalogoDigital.as_view(), name='catalogodigital'),
    path('ajrcutelaria', AJRCutelaria.as_view(), name='ajrcutelaria'),
    
]