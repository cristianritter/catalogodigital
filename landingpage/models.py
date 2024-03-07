from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
import ujson as json
from landingpage.model_fields import MultipleURLsField
from django.utils.text import slugify
from .utils import Storage
from catalogodigital import settings

class Categoria(models.Model):               #         
    class Meta:
        verbose_name = '     Ramos de atuação'
        verbose_name_plural = '     Ramos de atuação'
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome'])
        ]
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Cidade(models.Model):
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome'])
        ]
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Empresa(models.Model):
    class Meta:
        verbose_name = '     Empresa'
        verbose_name_plural = '     Empresas'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
    def clean(self):
        try:
            if self.website:
                urlValidate = URLValidator()
                urlValidate(self.website.split('#')[1])
        except:
            raise ValidationError(f'O Website não está configurado corretamente.')
        try:
            if '<iframe src=' in self.g_embbedmaps:
                https_part = self.g_embbedmaps.split('"')[1]
                if not 'https://www.google.com/maps/' in https_part:
                    raise Exception
                self.gmaps_link = https_part        
        except Exception as Err:
            raise ValidationError('O link do mapa do Google está incorreto.')
        try:
            nome_cidade_estado = self.address.split(',')[-1].strip()
            Cidade.objects.get(nome=nome_cidade_estado)
        except Cidade.DoesNotExist:
            raise ValidationError('A cidade {} não está cadastrada. Verifique o endereço'.format(nome_cidade_estado))    
    
    name = models.CharField(max_length=100, help_text='Nome da empresa')
    tagline = models.CharField(max_length=50, help_text='Texto em destaque que descreve a essência da marca.')
    owners = models.ManyToManyField(User, related_name='owners', help_text='Usuários que terão acesso de editor.')
    employees = models.ManyToManyField(User, blank=True, related_name='employees', help_text='Funcionários da empresa.')
    category = models.ForeignKey(Categoria, on_delete=models.PROTECT, help_text='Categoria dos serviços que a empresa oferece.')
    service_areas = models.ManyToManyField(Cidade)
    address = models.CharField(max_length=255, help_text='Precisa conter no mínimo: Bairro, Cidade - DF')
    opening_hours = models.CharField(max_length=100, help_text='Exemplo: Seg à Sex das 10h as 17h.')
    phone_numbers = models.CharField(max_length=50, help_text='Um ou mais números no modelo (11) 99887 6543 separados por vírgula.')
    is_whatsapp = models.BooleanField(help_text='Indica se o primeiro número informado é um contato do whatsapp.')
    e_mail = models.EmailField(blank=True, max_length=40, help_text='Email da empresa')
    social_media = MultipleURLsField(blank=True, max_length=250, help_text='Links das redes sociais separados por vírgula.')
    g_business = models.URLField(blank=True, max_length=50, help_text="Link obtido abrindo o google empresas e clicando em Share > Send a link. Ex: https://maps.app.goo.gl/pTZvag2fg7ytV74eA")
    g_embbedmaps = models.CharField(blank=True, max_length=500, help_text="Link obtido abrindo o google empresas e clicando em Share > Embed a map > Small.")
    website = models.CharField(max_length=150, blank=True, help_text='Nome do botão e link para para site. Ex. Conheça nossa Loja Virtual # https://minhaloja.com.br')
    def __str__(self):
        return self.name

class Page(models.Model):
    class Meta:
        abstract = True  # Define essa classe como abstrata para que não seja criada como tabela no banco de dados
    on_air = models.BooleanField(default=False, help_text='Indica se a página está no ar.')
   
class LandingPage(Page):
    class Meta:
        verbose_name = '    Landing Page'
        verbose_name_plural = '   Landing Pages'
        ordering = ['-on_air', 'empresa']
        #indexes = [
        #    models.Index(fields=['url']),
        #    models.Index(fields=['on_air'])
        #]

    def image_tag(self):
        from django.utils.html import mark_safe
        html_preview = ""
        bucket_link = Storage.get_bucket_url(settings.BUCKET_NAME)
        for file_name in Storage.get_bucket_file_list(settings.BUCKET_NAME, ''):
            # Adiciona a tag HTML para a imagem com o nome do arquivo ao lado
            html_preview += f'<div style="display: flex; align-items: center;">'
            html_preview += f'<img src="{bucket_link}/{file_name}" width="150" height="150" />'
            html_preview += f'<a href="{bucket_link}/{file_name}" target="_blank" style="margin-left: 10px;">{file_name}</a></div>'
        return mark_safe(html_preview)

    image_tag.short_description = 'Imagens no Bucket'

    
    def CidadeEstado(self):
        return f'{self.empresa.address.split(",")[-1].strip()}'
    
    def URL(self):
        city = self.CidadeEstado().split("-")[0]
        return f'{city}/{slugify(self.empresa.name)}'.lower()
    
    def Telefones(self):
        return self.empresa.phone_numbers
        
    def clean(self):
        try:
            if self.colunas_items:
                json.loads(self.colunas_items)
        except:
            raise ValidationError(f'O conteúdo de "Colunas items" está incorreto.')
    
    def save(self, *args, **kwargs):
        super(Page, self).save(*args, **kwargs)

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    lista_items = models.TextField(blank=True, default='[]', max_length=600,  help_text='Seção de lista da página. Um item por linha.')
    colunas_items = models.TextField(blank= True, default='{}', help_text='Seção de colunas da página. Dict no formato {"Título1":"Conteúdo1","Título2":"Conteúdo2"},...')
    carousel_size = models.IntegerField(help_text='Quantidade de imagens no carossel da página.')
    
    def __str__(self):
        return f'{self.empresa.name}'

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.nome

class Servico(models.Model):
    class Meta:
        verbose_name = '     Serviço sob agendamento'
        verbose_name_plural = '    Serviços sob agendamento'
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.IntegerField()  # em minutos
    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    def __str__(self):
        return f"{self.cliente} - {self.servico} - {self.data_hora}"
    