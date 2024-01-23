from django.urls import path
from .views import AJRCutelaria
app_name = 'landing'  # Substitua 'seu_app_nome' pelo nome real do seu aplicativo

print('entrou/n/n/n/n/n/n\n\n\n\n\n\n\n\n')
urlpatterns = [
    path('', AJRCutelaria.as_view(), name='index'),
]