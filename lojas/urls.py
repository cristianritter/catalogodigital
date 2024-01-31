from django.urls import path, re_path
from .views import BaseLoja, redirect_to_landingpage
from django.views.generic import TemplateView
app_name = 'lojas'
urlpatterns = [
  #  path('', redirect_to_landingpage, name='redirect_to_landingpage'),
  # path('cardapio_simples/', BaseLoja.as_view(), name="cardapio_simples"),
    path('robots.txt', TemplateView.as_view(template_name="robots-loja.txt", content_type="text/plain"), name="robots-loja.txt"),
    re_path(r'^.*$', BaseLoja.as_view(), name='DefaultLoja'),   

]