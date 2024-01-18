from django.urls import path
from .views import CatalogoDigital, AJRCutelaria, ResidencialVivaTorres, KelliSenaAcessoria, set_visitas, set_demo_view, DemoView, ListaPedidos

app_name = 'landing'  # Substitua 'seu_app_nome' pelo nome real do seu aplicativo

urlpatterns = [
    path('', CatalogoDigital.as_view(), name='index'),
    path('set_visitas/', set_visitas, name='set_visitas'),
    path('set_demo_view/', set_demo_view, name='set_demo_view'),
    path('demo_view/', DemoView.as_view(), name='demo_view'),
    path('lista_pedidos/', ListaPedidos.as_view(), name='lista_pedidos'),
    path('catalogo_digital/', CatalogoDigital.as_view(), name='catalogo_digital'),
    path('ajr_cutelaria/', AJRCutelaria.as_view(), name='ajr_cutelaria'),
    path('kelli_sena_assessoria/', KelliSenaAcessoria.as_view(), name='kelli_sena_assessoria'),
    path('residencial_viva_torres/', ResidencialVivaTorres.as_view(), name='residencial_viva_torres'),
]
