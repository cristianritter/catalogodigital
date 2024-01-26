from django.db import models

class LandingPageData(models.Model):
    #Dados técnicos
    url_cadastrado = models.CharField(max_length=50, help_text='O endereço final do link da página')
    num_imagens_carrousel = models.IntegerField(help_text='O número de imagens no carrossel')
    caminho_de_arquivos = models.CharField(max_length=100, help_text='cidade/nome_da_empresa')
    #Dados Gerais da empresa
    nome_empresa = models.CharField(max_length=30, help_text='Servirá como título da Página')
    descricao_curta = models.CharField(max_length=100, help_text='Resuma em uma sentença curta o que a empresa faz')
    meta_description = models.CharField(max_length=160, help_text='Uma descrição que vai aparecer para o usuário durante a busca')
    lista_titulo = models.CharField(max_length=50, help_text='Pode ser usado o título: "Produtos e Serviços"')
    lista_items = models.TextField(help_text='Digite os itens da lista de produtos ou serviços separados por vírgula')
    colunas_items = models.TextField(help_text='Subtitulos # conteúdo # (cada dupla vira uma coluna no layout final)')
    numeros_telefone = models.CharField(max_length=50, help_text='Digite os números de telefone')
    email_contato = models.EmailField(blank=True, help_text='Digite o email da empresa, se houver')
    endereco = models.CharField(blank=True, max_length=100)
    horario_atendimento = models.CharField(max_length=100, help_text='Digite o horário de atendimento')
    # Links (usando URLField)
    whats_link = models.URLField()
    reviews_link = models.URLField()
    gmaps_link = models.URLField(max_length=500)

    def __str__(self):
        return self.nome_empresa


"""class PageViewsCounter(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.IntegerField(default=0)
    def increment(self):
        self.value += 1
        self.save()
"""