from django.urls import path
from .views import render_root_page, Homepage, BaseCardapioSimples, SejaNossoCliente, AJRCutelaria, set_visitas, set_demo_view, DemoView
#from .views import ResidencialVivaTorres, KelliSenaAcessoria, ListaPedidos
app_name = 'landing'  # Substitua 'seu_app_nome' pelo nome real do seu aplicativo

urlpatterns = [
    path('cardapio_simples/', BaseCardapioSimples.as_view(), name='cardapio_simples'),
    path('', render_root_page, name='index'),
    path('home', Homepage.as_view(), name='home'),
    path('set_visitas/', set_visitas, name='set_visitas'),
    path('set_demo_view/', set_demo_view, name='set_demo_view'),
    path('demo_view/', DemoView.as_view(), name='demo_view'),
#   path('lista_pedidos/', ListaPedidos.as_view(), name='lista_pedidos'),
    path('seja_nosso_cliente/', SejaNossoCliente.as_view(), name='seja_nosso_cliente'),
    path('ajr_cutelaria/', AJRCutelaria.as_view(), name='ajr_cutelaria'),
#   path('kelli_sena_assessoria/', KelliSenaAcessoria.as_view(), name='kelli_sena_assessoria'),
#   path('residencial_viva_torres/', ResidencialVivaTorres.as_view(), name='residencial_viva_torres'),
]
