from django.db import models
from landingpage.models import Page, Empresa

class Store(Page):
    class Meta:
        verbose_name = '   Store'
        verbose_name_plural = '   Stores'
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=100, help_text='Tema central na página')
    paragrafo = models.TextField(max_length=600, help_text='Parágrafo de boas vindas')
    produtos = models.TextField(help_text='Informações do produto passadas no formato Json. Ex: {"pizza": ["Pizza de Calabresa", "Calabresa, Queijo Chedar e massa especial", 59.90, "nome_do_arquivo"]}')   
    def __str__(self):
        return self.empresa.name
    
class Shelf(models.Model):
    class Meta:
        verbose_name = '  Shelf'
        verbose_name_plural = '  Shelves'
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Item(models.Model):
    class Meta:
        verbose_name = ' Item'
        verbose_name_plural = ' Items'
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    imagem_url = models.CharField(max_length=255, blank=True, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    session_key = models.CharField(max_length=40)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Hub(Page):
    class Meta:
        verbose_name = 'Concentrador'
        verbose_name_plural = 'Concentradores'
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, help_text="Nome do Food Park centralizador")
    slogam = models.CharField(max_length=100, help_text="Slogam do Food Park centralizador")
    lojas = models.ManyToManyField(Store)
    def __str__(self):
        return self.empresa.name

    
   