from django.urls import path
from .views import BaseLoja, redirect_to_landingpage
app_name = 'lojas'
urlpatterns = [
    path('', redirect_to_landingpage, name='redirect_to_landingpage'),
    path('cardapio_simples/', BaseLoja.as_view(), name="cardapio_simples"),

]