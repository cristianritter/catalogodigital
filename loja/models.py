from django.db import models
from landingpage.models import Page, Empresa



class Loja(Page):
    class Meta:
        verbose_name = 'Registro de Loja'
        verbose_name_plural = 'Registros de Lojas'
    #Dados Gerais da empresa
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=100, help_text='Tema central na página')
    paragrafo = models.TextField(max_length=600, help_text='Parágrafo de boas vindas')
    produtos = models.TextField(help_text='Informações do produto passadas no formato Json. Ex: {"pizza": ["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "nome_do_arquivo"]}')   
    def __str__(self):
        return self.empresa.name
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Loja, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    session_key = models.CharField(max_length=40)
    store = models.ForeignKey(Loja, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Hub(Page):
    class Meta:
        verbose_name = 'Registro de Hub'
        verbose_name_plural = 'Registros de Hubs'
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, help_text="Nome do Food Park centralizador")
    slogam = models.CharField(max_length=100, help_text="Slogam do Food Park centralizador")
    lojas = models.ManyToManyField(Loja)

    def __str__(self):
        return self.empresa.name

    
   