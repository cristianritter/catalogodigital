from django.urls import path
from landing.views import AJRCutelaria

urlpatterns = [
    path('', AJRCutelaria.as_view(), name='index'),
]

