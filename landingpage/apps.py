from django.apps import AppConfig
from os import getenv
from django.core.cache import cache

class LandingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "landingpage"
    verbose_name = 'empresas e serviços'

    def ready(self):
        #import landingpage.signals # não pode retirar, usado para limpar a cache
        from django.contrib.auth.models import Permission
        #from .models import LandingPagePermission
        from landingpage.models import LandingPage
        from django.contrib.contenttypes.models import ContentType
    
        Permission.objects.get_or_create(
            codename='can_access_own_products',
            name='Can Access Own Products',
            content_type=ContentType.objects.get_for_model(LandingPage),
        )