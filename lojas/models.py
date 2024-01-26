from django.db import models

class LojaData(models.Model):
    #Dados técnicos
    url_cadastrado = models.CharField(max_length=50, help_text='O endereço final do link da página')
    caminho_de_arquivos = models.CharField(max_length=100, help_text='cidade/nome_da_empresa')
    #Dados Gerais da empresa
    meta_description = models.CharField(max_length=160, help_text='Uma descrição que vai aparecer para o usuário durante a busca')
    nome_empresa = models.CharField(max_length=30, help_text='Nome ao lado da logomarca')
    slogam = models.CharField(max_length=100, help_text='Slogam abaixo do nome da empresa')
    titulo = models.CharField(max_length=100, help_text='Tema central na página')
    paragrafo = models.TextField(max_length=1000, help_text='Um parágrafo descrevendo a loja')
    produtos = models.TextField(help_text='Informações do produto passadas no formato Json. Ex:\
                                {"pizza": [["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "01.jpg"]\]}')
    #Links
    link_facebook = models.URLField(blank=True)
    link_instagram = models.URLField(blank=True)
    link_facebook = models.URLField(blank=True)
    link_whats = models.URLField(blank=True)
    
    def __str__(self):
        return self.url_cadastrado
