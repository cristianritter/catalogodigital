from django.urls import path
from .views import BaseLoja

urlpatterns = [
    path('cardapio_simples/', BaseLoja.as_view(), name="cardapio_simples"),
]