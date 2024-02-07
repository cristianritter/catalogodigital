from django.urls import path, re_path
from .views import HubView, LojaSitemap, LojaView, home
from django.views.generic import TemplateView
from django.contrib.sitemaps import views as sitemap_views

app_name = 'loja'
urlpatterns = [
  #  path('', redirect_to_landingpage, name='redirect_to_landingpage'),
  # path('cardapio_simples/', BaseLoja.as_view(), name="cardapio_simples"),
    path('', home, name='home_redirect'),
 #   path('hub', TemplateView.as_view(template_name='hub.html'), name='hub_lojas'),
    path('robots.txt', TemplateView.as_view(template_name="robots-loja.txt", content_type="text/plain"), name="robots-loja.txt"),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'meu_sitemap': LojaSitemap}}),
    re_path(r'^hub/(?P<url>.*)$', HubView.as_view(), name='Hub'),
    re_path(r'^(?P<url>.*)$', LojaView.as_view(), name='Loja'),   

]