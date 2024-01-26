from django.urls import path
from .views import Homepage, SejaNossoCliente, AJRCutelaria, set_visitas, set_demo_view, DemoView
app_name = 'landingpage'  # Substitua 'seu_app_nome' pelo nome real do seu aplicativo

urlpatterns = [
### Urls do sistema
    path('home', Homepage.as_view(), name='home'),
    path('set_visitas/', set_visitas, name='set_visitas'),
    path('set_demo_view/', set_demo_view, name='set_demo_view'),
    path('demonstracao/', DemoView.as_view(), name='demo_view'),
    path('seja_nosso_cliente/', SejaNossoCliente.as_view(), name='seja_nosso_cliente'),

### Urls de clientes
    path('ajr_cutelaria/', AJRCutelaria.as_view(), name='ajr_cutelaria'),
]
