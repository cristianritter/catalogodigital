from django.urls import path, re_path
from .views import BaseLoja
from django.views.generic import TemplateView
app_name = 'lojas'
urlpatterns = [
    path('', TemplateView.as_view(template_name="404-wall-e.html"), name="lojas-not-found"),
    path('robots.txt', TemplateView.as_view(template_name="robots-loja.txt", content_type="text/plain"), name="robots-loja.txt"),
    re_path(r'^.*$', BaseLoja.as_view(), name='DefaultLoja'),   

]