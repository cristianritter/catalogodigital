from django.urls import path, re_path
from .views import LandingPageView, Homepage, RootSitemap, favicon_view
from django.views.generic import TemplateView
from django.contrib.sitemaps import views as sitemap_views

app_name = 'landingpage'  

urlpatterns = [
    path('home', Homepage.as_view(), name='home'),
    path('favicon.ico', favicon_view),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'meu_sitemap': RootSitemap}}),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots.txt"),
    re_path(r'^.*$', LandingPageView.as_view(), name='LandingPageView'),   
]

