from django.db import models
from landingpage.models import Page

class Loja(Page):
    class Meta:
        verbose_name = 'Registro de Loja'
        verbose_name_plural = 'Registros de Lojas'
    #Dados Gerais da empresa
    slogam = models.CharField(max_length=100, help_text='Slogam abaixo do nome da empresa')
    titulo = models.CharField(max_length=100, help_text='Tema central na página')
    paragrafo = models.TextField(max_length=1000, help_text='Um parágrafo descrevendo a loja')
    produtos = models.TextField(help_text='Informações do produto passadas no formato Json. Ex: {"pizza": ["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "nome_do_arquivo"]}')   
    def __str__(self):
        return self.url
    
class Hub(Page):
    class Meta:
        verbose_name = 'Registro de Hub'
        verbose_name_plural = 'Registros de Hubs'
    nome = models.CharField(max_length=100, help_text="Nome do Food Park centralizador")
    slogam = models.CharField(max_length=100, help_text="Slogam do Food Park centralizador")
    lojas = models.ManyToManyField(Loja)

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    
   