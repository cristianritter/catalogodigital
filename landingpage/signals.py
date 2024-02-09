from django.db.models.signals import post_save
from django.dispatch import receiver
from landingpage.models import LandingPage
from django.core.cache import cache

@receiver(post_save, sender=LandingPage)
def minha_funcao_de_instrucao(sender, instance, created, **kwargs):
    cache.delete(f'{instance.url}.landing') # atualiza a cache ao editar o modelo