from django.urls import path
from .views import CatalogoDigital, AJRCutelaria, ResidencialVivaTorres, KelliSenaAcessoria
from .views import  set_visitas, set_demo_view, DemoView, ListaPedidos

urlpatterns = [
    path('set_visitas/', set_visitas, name='set_visitas'),
    path('set_demo_view/', set_demo_view, name='set_demo_view'),
    path('demo_view', DemoView.as_view(), name='demo_view'),
    path('lista_pedidos', ListaPedidos.as_view(), name='lista_pedidos'),
    path('', CatalogoDigital.as_view(), name='catalogodigital'),
    path('index', CatalogoDigital.as_view(), name='catalogodigital'),
    path('home', CatalogoDigital.as_view(), name='catalogodigital'),
    path('catalogodigital', CatalogoDigital.as_view(), name='catalogodigital'),
    path('ajrcutelaria', AJRCutelaria.as_view(), name='ajrcutelaria'),
    path('kellisenaassessoria', KelliSenaAcessoria.as_view(), name='kellisenaassessoria'),
    path('residencialvivatorres', ResidencialVivaTorres.as_view(), name='residencialvivatorres'),
    
]