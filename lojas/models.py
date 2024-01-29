from django.db import models
from landingpages.models import PageWithBucket

class Loja(PageWithBucket):
    class Meta:
        verbose_name = 'Registro de Loja'
        verbose_name_plural = 'Registros de Lojas'
    #Dados Gerais da empresa
    meta_description = models.CharField(max_length=160, help_text='Uma descrição que vai aparecer para o usuário durante a busca')
    slogam = models.CharField(max_length=100, help_text='Slogam abaixo do nome da empresa')
    titulo = models.CharField(max_length=100, help_text='Tema central na página')
    paragrafo = models.TextField(max_length=1000, help_text='Um parágrafo descrevendo a loja')
    produtos = models.TextField(help_text='Informações do produto passadas no formato Json. Ex:\
                                {"pizza": [["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "01.jpg"]\]}')   
    def __str__(self):
        return self.url_cadastrado
