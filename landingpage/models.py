from django.db import models

class PageWithBucket(models.Model):
    class Meta:
        abstract = True  # Define essa classe como abstrata para que não seja criada como tabela no banco de dados
    on_air = models.BooleanField(help_text='Indica se a página está no ar.')
    endereco_bucket = models.CharField(max_length=200, help_text='https://gjvoxpezczvyqbnmonap.supabase.co/storage/v1/object/public/conecta_bucket/')
    url_cadastrado = models.CharField(max_length=50, help_text='O endereço final do link da página')
    meta_description = models.CharField(blank=True, max_length=160, help_text='Uma descrição que vai aparecer para o usuário durante a busca')
    nome_empresa = models.CharField(max_length=50, help_text='Servirá como título da página')
    #Links
    link_whats = models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=SEU_NUMERO_DE_TELEFONE')
    link_facebook = models.URLField(blank=True)
    link_instagram = models.URLField(blank=True)
    link_facebook = models.URLField(blank=True)
    
class LandingPage(PageWithBucket):
    class Meta:
        verbose_name = 'Registro de Landing Page'
        verbose_name_plural = 'Registros de Landing Pages'
    #Dados técnicos
    nomes_arquivos_imagens = models.CharField(blank=True, max_length=300, help_text='nomes dos arquivos, separados por virgula')
    #Dados Gerais da empresa
    descricao_curta = models.CharField(max_length=100, help_text='Resuma em uma sentença curta o que a empresa faz')
    lista_titulo = models.CharField(blank=True, max_length=50, help_text='Título da lista. Ex: "Produtos e Serviços"')
    lista_items = models.TextField(blank=True, help_text='Itens da lista em formato de list ["abc", "cde"]')
    colunas_items = models.TextField(blank=True, help_text='Conteúdo adicional no formato de dict. {"key": "value", "key2": "value2"}')
    numeros_telefone = models.CharField(blank=True, max_length=50, help_text='Números de telefone no formato (12) 98765 4321')
    email_contato = models.EmailField(blank=True, help_text='Email da empresa, se houver')
    endereco = models.CharField(blank=True, max_length=100, help_text="Endereço ou região da ede da empresa")
    horario_atendimento = models.CharField(blank=True, max_length=100, help_text='Horário de funcionamento')
    # Links (usando URLField)
    link_loja = models.URLField(blank=True, help_text="Link para loja virtual, se houver")
    reviews_link = models.URLField(blank=True, help_text="Link para os reviews do google, se houver")
    gmaps_link = models.URLField(blank=True, max_length=500, help_text="Link para os mapas 'embedded' no formato 'https:\\....br' ")
    def __str__(self):
        return self.url_cadastrado


"""class PageViewsCounter(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.IntegerField(default=0)
    def increment(self):
        self.value += 1
        self.save()
"""