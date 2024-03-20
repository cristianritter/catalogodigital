from django.db import models
from landingpage.models import Page, Empresa
from landingpage.utils import Generate, Storage


class Store(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.destFolder = 'stores/' + str(self.id)  
    class Meta:
        verbose_name = '   Store'
        verbose_name_plural = '   Stores'

    def web_address(self):
        return Generate._generate_web_address(self.empresa.name, self.empresa.address, prefix='hub/')

    def image_tag(self):
        itemImagePath = Storage.get_image_tag(self.destFolder)
        return itemImagePath
    image_tag.short_description = 'Imagens no Bucket'


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.destFolder = 'items/' + str(self.id)   
    class Meta:
        verbose_name = ' Item'
        verbose_name_plural = ' Items'

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    imagem_url = models.CharField(max_length=255, blank=True, null=True)
    image_filename = models.CharField(max_length=50, blank=True, editable=False)
    shelf = models.ForeignKey(Shelf, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
    
    def image_tag(self):
        itemImagePath = Storage.get_image_tag(self.destFolder)
        return itemImagePath
    image_tag.short_description = 'Imagens no Bucket'

    def save(self, *args, **kwargs):
        image_path = Generate._generate_company_path(self.shelf.store.empresa.name, self.shelf.store.empresa.address) + '/store/shelfs/items/'
        self.image_filename=Storage.get_bucket_file_list(image_path)[0]
        super(Item, self).save(*args, **kwargs)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Hub(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.destFolder = 'hubs/' + str(self.id)   
    class Meta:
        verbose_name = 'Concentrador'
        verbose_name_plural = 'Concentradores'

    def web_address(self):
        return Generate._generate_web_address(self.empresa.name, self.empresa.address, prefix='hub/')

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    lojas = models.ManyToManyField(Store)
    
    def __str__(self):
        return self.empresa.name
    
    def image_tag(self):
        itemImagePath = Storage.get_image_tag(self.destFolder)
        return itemImagePath
    image_tag.short_description = 'Imagens no Bucket'


    
   