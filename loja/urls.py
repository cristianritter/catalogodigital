from django.urls import path, re_path
from .views import HubView, LojaView, home
from django.views.generic import TemplateView

app_name = 'loja'
urlpatterns = [
  #  path('', redirect_to_landingpage, name='redirect_to_landingpage'),
  # path('cardapio_simples/', BaseLoja.as_view(), name="cardapio_simples"),
    path('', home, name='home_redirect'),
 #   path('hub', TemplateView.as_view(template_name='hub.html'), name='hub_lojas'),
    path('robots.txt', TemplateView.as_view(template_name="robots-loja.txt", content_type="text/plain"), name="robots-loja.txt"),
    re_path(r'^hub/(?P<pagina>.*)$', HubView.as_view(), name='Hub'),
    re_path(r'^(?P<pagina>.*)$', LojaView.as_view(), name='Loja'),   

]