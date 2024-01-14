from django.urls import path
from .views import CatalogoDigital, AJRCutelaria, set_visitas, ResidencialVivaTorres

urlpatterns = [
    path('set-visitas/', set_visitas, name='set_visitas'),
    path('', CatalogoDigital.as_view(), name='catalogodigital'),
    path('index', CatalogoDigital.as_view(), name='catalogodigital'),
    path('home', CatalogoDigital.as_view(), name='catalogodigital'),
    path('catalogodigital', CatalogoDigital.as_view(), name='catalogodigital'),
    path('ajrcutelaria', AJRCutelaria.as_view(), name='ajrcutelaria'),
    path('residencialvivatorres', ResidencialVivaTorres.as_view(), name='residencialvivatorres'),
    
]