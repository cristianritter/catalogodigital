from django.urls import path
from .views import CatalogoDigital, AJRCutelaria, set_visitas

urlpatterns = [
    path('set-visitas/', set_visitas, name='set_visitas'),
    path('', CatalogoDigital.as_view(), name='catalogodigital'),
    path('index', CatalogoDigital.as_view(), name='catalogodigital'),
    path('home', CatalogoDigital.as_view(), name='catalogodigital'),
    path('catalogodigital', CatalogoDigital.as_view(), name='catalogodigital'),
    path('ajrcutelaria', AJRCutelaria.as_view(), name='ajrcutelaria'),
    
]