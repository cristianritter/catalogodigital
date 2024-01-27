from django.urls import path, re_path
from .views import DefaultLandingPage, Homepage, set_visitas
from django.views.generic import TemplateView

app_name = 'landingpages'  

urlpatterns = [
### Urls do sistema
    path('home/', Homepage.as_view(), name='home'),
    path('set_visitas/', set_visitas, name='set_visitas'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots.txt"),
    re_path(r'^.*$', DefaultLandingPage.as_view(), name='DefaultLandingPage'),   
]
