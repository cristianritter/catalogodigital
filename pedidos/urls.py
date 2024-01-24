from django.urls import path
from .views import hello_world, BaseCardapioSimples

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('cardapio_simples/', BaseCardapioSimples.as_view(), name="cardapio_simples")
]