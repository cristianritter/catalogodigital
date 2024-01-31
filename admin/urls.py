from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="robots-adm.txt", content_type="text/plain"), name="robots-adm.txt"),
    path("", admin.site.urls),
]
