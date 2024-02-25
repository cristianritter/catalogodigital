import ujson as json
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class MultipleURLsField(models.TextField):          # Created Field Type For Multiple URL At The Same Field
    description = "Field to store multiple URLs separated by comma"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate_urls(self, value):
        urls = value.split(',')
        validate_url = URLValidator()
        for url in urls:
            url = url.strip()
            if url:
                validate_url(url)
            else:
                raise ValidationError('Empty URL is not allowed')

    def clean(self, value, model_instance):
        self.validate_urls(value)
        return value


class CategoriaServico(models.Model):               #         
    class Meta:
        verbose_name = 'Categoria de Serviço'
        verbose_name_plural = 'Categorias de Serviços'
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome'])
        ]
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Cidade(models.Model):
    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome'])
        ]

    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome


class Empresa(models.Model):
    class Meta:
        verbose_name = 'Cadastro de Negócio'
        verbose_name_plural = 'Cadastro de Negócios'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
    category = models.ForeignKey(CategoriaServico, on_delete=models.PROTECT, help_text='Categoria dos serviços que a empresa oferece.')
    owners = models.ManyToManyField(User, help_text='Usuários que terão acesso de editor.')
    name = models.CharField(max_length=100, help_text='Nome da empresa')
    tagline = models.CharField(max_length=50, help_text='Texto em destaque que descreve a essência da marca.')
    address = models.CharField(max_length=255, help_text='Precisa conter no mínimo: Bairro, Cidade - DF')
    phone_numbers = models.CharField(max_length=50, help_text='Um ou mais números no modelo 55 11 99887 6543 separados por vírgula.')
    is_whatsapp = models.BooleanField(help_text='Indica se o primeiro número informado é um contato do whatsapp.')
    e_mails = models.EmailField(blank=True, max_length=40, help_text='Email da empresa')
    social_media_links = MultipleURLsField(blank=True, max_length=250, help_text='Links das redes sociais separados por vírgula.')
    opening_hours = models.CharField(max_length=100, help_text='Exemplo: Seg à Sex das 10h as 17h.')
    def __str__(self):
        return self.name

class Page(models.Model):
    class Meta:
        abstract = True  # Define essa classe como abstrata para que não seja criada como tabela no banco de dados
    on_air = models.BooleanField(default=False, help_text='Indica se a página está no ar.')
    url = models.CharField(max_length=50, help_text='A parte personalizada do endereço no final do link da página')
    link_whats = models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=')
    link_facebook = models.URLField(blank=True, help_text='Link para a página do facebook')
    link_instagram = models.URLField(blank=True, help_text='Link para a página do instagram')
    nome_empresa = models.CharField(max_length=50, help_text='Nome da empresa, da loja ou do concentrador')
    #redes_sociais = models.TextField(help_text='Links das redes sociais separados por linha')

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
        ordering = ['-on_air', 'nome_empresa']
        indexes = [
            models.Index(fields=['url']),
            models.Index(fields=['on_air'])
        ]

    def clean(self):
        try:
            nome_cidade_estado = self.endereco.split(',')[-1].strip()
            cidade = Cidade.objects.get(nome=nome_cidade_estado)
        #    self.cidades.add(cidade)
        except Cidade.DoesNotExist:
            raise ValidationError('A cidade {} não está cadastrada. Verifique o endereço'.format(nome_cidade_estado))
        except Exception as err:
            raise ValidationError('Ocorreu um erro ao adicionar a cidade: {}'.format(err))

        try:
            self.url.split('/')[1]
        except:
            cidade = slugify(self.endereco.split(',')[-1].split('-')[0])
            self.url = f'{cidade}/{self.url}'
        
        try:
            if self.colunas_items:
                json.loads(self.colunas_items)
        except:
            raise ValidationError(f'O conteúdo de "Colunas items" está incorreto.')
        
        try:
            if self.link_loja:
                self.link_loja.split('#')[1]
        except:
            raise ValidationError(f'O conteúdo de "Link loja" está incorreto.')
        
        try:
            if '<iframe src=' in self.gmaps_link:
                https_part = self.gmaps_link.split('"')[1]
                if not 'https://www.google.com/maps/' in https_part:
                    raise Exception
                self.gmaps_link = https_part        
        except Exception as Err:
            raise ValidationError('O conteúdo de "Gmaps link" está incorreto.')

    def save(self, *args, **kwargs):
        #self.full_clean()
        super(Page, self).save(*args, **kwargs)

    #Dados Gerais da empresa
    descricao_curta = models.CharField(max_length=100, help_text='Texto acima do nome da empresa(SubHeader). Síntese da atividade principal. (Obrigatório conter as PALAVRAS CHAVES)')
    lista_items = models.TextField(blank=True, default='[]', max_length=600,  help_text='Seção de lista da página. Um item por linha.')
    colunas_items = models.TextField(blank= True, default='{}', help_text='Seção de colunas da página. Dict no formato {"Título1":"Conteúdo1","Título2":"Conteúdo2"},...')
    numeros_telefone = models.CharField(blank=True, max_length=50, help_text='Ex: (12) 98765 4321 (São permitidos múltiplos números)')
    email_contato = models.EmailField(blank=True, help_text='Ex: nome@empresa.com.br')
    endereco = models.CharField(blank=True, max_length=100, help_text="Ex: Rua Duque de Caxias, 237, Centenário, Sapiranga - RS")
    cidades = models.ManyToManyField(Cidade)
    categoria_servico = models.ForeignKey(CategoriaServico, blank=True, on_delete=models.PROTECT)
    horario_atendimento = models.CharField(blank=True, max_length=100, help_text='Ex: Seg à Sex das 10h as 17h.')

    carousel_size = models.IntegerField(help_text='Quantidade de imagens no carossel da página.')
    
    # Links (usando URLField)
    link_loja = models.CharField(max_length=150, blank=True, help_text='Nome do botão e link para para site externo. Conheça nossa Loja Virtual#https://minhaloja.com.br')
    reviews_link = models.URLField(blank=True, help_text="Link obtido abrindo o google empresas e clicando em Share > Send a link. Ex: https://maps.app.goo.gl/pTZvag2fg7ytV74eA")
    gmaps_link = models.CharField(blank=True, max_length=500, help_text="Link obtido abrindo o google empresas e clicando em Share > Embed a map > Small.")
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.url

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.IntegerField()  # em minutos

    def __str__(self):
        return self.nome
    

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    
    def __str__(self):
        return f"{self.cliente} - {self.servico} - {self.data_hora}"




    
class LandingPagePermission(models.Model):
    class Meta:
        permissions = [
            ("can_access_own_products", "Can Access Own Products"),
        ]


