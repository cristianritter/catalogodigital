from django.http import HttpRequest
from django.urls import path, re_path
from .views import DefaultLandingPage, Sitemap
from django.views.generic import TemplateView
from django.contrib.sitemaps import views as sitemap_views

app_name = 'landingpages'  



urlpatterns = [
#    path('home/', Homepage.as_view(), name='home'),
#   path('set_visitas/', set_visitas, name='set_visitas'),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'meu_sitemap': Sitemap}}),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots.txt"),
    re_path(r'^.*$', DefaultLandingPage.as_view(), name='DefaultLandingPage'),   
]
