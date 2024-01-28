from django.db import models

class LandingPageData(models.Model):
    #Dados técnicos
    on_air = models.BooleanField(help_text='Indica se a página está no ar.')
    url_cadastrado = models.CharField(max_length=50, help_text='O endereço final do link da página')
    endereco_bucket = models.CharField(blank=True, max_length=200, help_text='https://gjvoxpezczvyqbnmonap.supabase.co/storage/v1/object/public/conecta_bucket/')
    nomes_arquivos_imagens = models.TextField(blank=True, help_text='Links para os arquivos, separados por virgula')
    #Dados Gerais da empresa
    nome_empresa = models.CharField(max_length=50, help_text='Servirá como título da Página')
    descricao_curta = models.CharField(max_length=100, help_text='Resuma em uma sentença curta o que a empresa faz')
    meta_description = models.CharField(max_length=160, help_text='Uma descrição que vai aparecer para o usuário durante a busca')
    lista_titulo = models.CharField(max_length=50, help_text='Pode ser usado o título: "Produtos e Serviços"')
    lista_items = models.TextField(help_text='Digite os itens da lista de produtos ou serviços separados por #')
    colunas_items = models.TextField(help_text='Subtitulos # conteúdo # (cada dupla vira uma coluna no layout final)')
    numeros_telefone = models.CharField(max_length=50, help_text='Digite os números de telefone')
    email_contato = models.EmailField(blank=True, help_text='Digite o email da empresa, se houver')
    endereco = models.CharField(blank=True, max_length=100)
    horario_atendimento = models.CharField(max_length=100, help_text='Digite o horário de atendimento')
    # Links (usando URLField)
    link_loja = models.URLField(blank=True)
    whats_link = models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=SEU_NUMERO_DE_TELEFONE')
    reviews_link = models.URLField(blank=True)
    gmaps_link = models.URLField(blank=True, max_length=500)
    def __str__(self):
        return self.url_cadastrado


"""class PageViewsCounter(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.IntegerField(default=0)
    def increment(self):
        self.value += 1
        self.save()
"""