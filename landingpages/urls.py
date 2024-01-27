from django.urls import path, re_path
from .views import DefaultLandingPage, Homepage, set_visitas
app_name = 'landingpage'  # Substitua 'seu_app_nome' pelo nome real do seu aplicativo

urlpatterns = [
### Urls do sistema
    path('home', Homepage.as_view(), name='home'),
    path('set_visitas/', set_visitas, name='set_visitas'),
    re_path(r'^.*$', DefaultLandingPage.as_view(), name='DefaultLandingPage'),   
  
]
