from django.urls import path
from landing_pages.views import AJRCutelaria

urlpatterns = [
    path('', AJRCutelaria.as_view(), name='index'),
]

