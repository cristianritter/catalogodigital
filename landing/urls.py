from django.urls import path
from .views import CatalogoDigital, AJRCutelaria, set_visitas, ResidencialVivaTorres, ListaPedidos, KelliSenaAcessoria

urlpatterns = [
    path('set-visitas/', set_visitas, name='set_visitas'),
    path('lista-pedidos', ListaPedidos.as_view(), name='lista-pedidos'),
    path('', CatalogoDigital.as_view(), name='catalogodigital'),
    path('index', CatalogoDigital.as_view(), name='catalogodigital'),
    path('home', CatalogoDigital.as_view(), name='catalogodigital'),
    path('catalogodigital', CatalogoDigital.as_view(), name='catalogodigital'),
    path('ajrcutelaria', AJRCutelaria.as_view(), name='ajrcutelaria'),
    path('kellisenaassessoria', KelliSenaAcessoria.as_view(), name='kellisenaassessoria'),
    path('residencialvivatorres', ResidencialVivaTorres.as_view(), name='residencialvivatorres'),
    
]