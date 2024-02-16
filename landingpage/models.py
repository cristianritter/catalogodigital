from django.db import models
from django.core.exceptions import ValidationError
import json

class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class CategoriaServico(models.Model):
    class Meta:
        verbose_name = 'Categoria de Serviço'
        verbose_name_plural = 'Categorias de Serviços'

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Page(models.Model):
    class Meta:
        abstract = True  # Define essa classe como abstrata para que não seja criada como tabela no banco de dados
    on_air = models.BooleanField(default=False, help_text='Indica se a página está no ar.')
    url = models.CharField(max_length=50, help_text='A parte personalizada do endereço no final do link da página')
    link_whats = models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=')
    link_facebook = models.URLField(blank=True, help_text='Link para a página do facebook')
    link_instagram = models.URLField(blank=True, help_text='Link para a página do instagram')
    nome_empresa = models.CharField(max_length=50, help_text='Nome da empresa, da loja ou do concentrador')

    def clean(self):
        if ' ' in self.url:
            raise ValidationError(f'O conteúdo de "Url: {self.url}" não pode conter espaços em branco.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Page, self).save(*args, **kwargs)

class LandingPage(Page):
    class Meta:
        verbose_name = 'Registro de Landing Page'
        verbose_name_plural = 'Registros de Landing Pages'

    def clean(self):
        try:
            if self.lista_items:
                json.loads(self.lista_items)
        except:
            raise ValidationError(f'O conteúdo de "Lista items" está incorreto.')
        try:
            if self.colunas_items:
                json.loads(self.colunas_items)
        except:
            raise ValidationError(f'O conteúdo de "Colunas items" está incorreto.')
        try:
            if self.link_loja:
                json.loads(self.link_loja)
        except:
            raise ValidationError(f'O conteúdo de "Link loja" está incorreto.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Page, self).save(*args, **kwargs)

    #Dados Gerais da empresa
    descricao_curta = models.CharField(max_length=100, help_text='Texto acima do nome da empresa(SubHeader). Síntese da atividade principal. (Obrigatório conter as PALAVRAS CHAVES)')
    trend_words = models.CharField(max_length=300, help_text='Palavras chaves consultadas no Google Trend')
    lista_items = models.TextField(blank=True, default='[]', max_length=600,  help_text='Seção de lista da página. Lista no formato ["item1","item2",...]')
    colunas_items = models.TextField(blank= True, default='{}', help_text='Seção de colunas da página. Dict no formato {"Título1":"Conteúdo1","Título2":"Conteúdo2"},...')
    numeros_telefone = models.CharField(blank=True, max_length=50, help_text='Ex: (12) 98765 4321 (São permitidos múltiplos números)')
    email_contato = models.EmailField(blank=True, help_text='Ex: nome@empresa.com.br')
    endereco = models.CharField(blank=True, max_length=100, help_text="Ex: Rua Duque de Caxias, 237")
    cidades = models.ManyToManyField(Cidade)
    categoria_servico = models.ForeignKey(CategoriaServico, blank=True, on_delete=models.PROTECT)
    horario_atendimento = models.CharField(blank=True, max_length=100, help_text='Ex: Seg à Sex das 10h as 17h.')

    carousel_size = models.IntegerField(help_text='Quantidade de imagens no carossel da página.')
    
    # Links (usando URLField)
    link_loja = models.TextField(default='{}', max_length=150, blank=True, help_text='Nome do botão e link para para site externo. Dict no formato {"Conheça nossa Loja Virtual":"https://minhaloja.com.br" }')
    reviews_link = models.URLField(blank=True, help_text="Link obtido abrindo o google empresas e clicando em Share > Send a link. Ex: https://maps.app.goo.gl/pTZvag2fg7ytV74eA")
    gmaps_link = models.CharField(blank=True, max_length=500, help_text="Link obtido abrindo o google empresas e clicando em Share > Embed a map > Small.")
    def __str__(self):
        return self.url

