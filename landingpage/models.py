from django.db import models

class Page(models.Model):
    class Meta:
        abstract = True  # Define essa classe como abstrata para que não seja criada como tabela no banco de dados
    on_air = models.BooleanField(help_text='Indica se a página está no ar.')
    url = models.CharField(max_length=50, help_text='A parte personalizada do endereço no final do link da página')
    meta_description = models.CharField(blank=True, max_length=160, help_text='Descrição do site que vai aparecer para o usuário durante a busca.')
    link_whats = models.URLField(blank=True, help_text='https://api.whatsapp.com/send?phone=5199876543')
    link_facebook = models.URLField(blank=True, help_text='Link para a página do facebook')
    link_instagram = models.URLField(blank=True, help_text='Link para a página do instagram')
    nome_empresa = models.CharField(max_length=50, help_text='Nome da empresa, da loja ou do concentrador')

class LandingPage(Page):
    class Meta:
        verbose_name = 'Registro de Landing Page'
        verbose_name_plural = 'Registros de Landing Pages'
    carousel_size = models.IntegerField(help_text='Quantidade de imagens no carossel da página.')
    #Dados Gerais da empresa
    descricao_curta = models.CharField(max_length=100, help_text='Texto acima do nome da empresa(SubHeader). Síntese da atividade principal. (Obrigatório conter as PALAVRAS CHAVES)')
    resumo_chave = models.TextField(max_length=300, help_text='Este resumo deve ser uma descrição bem clara e objetiva (Obrigatório conter variações das PALAVRAS CHAVES e o NOME DA CIDADE).')
    lista_items = models.TextField(blank=True, max_length=600,  help_text='Seção de lista da página. Dict no formato {"Título da lista": ["item1","item2",...]')
    colunas_items = models.TextField(blank=True, help_text='SEeão de colunas da página. Dict no formato {"Título1":"Conteúdo1","Título2":"Conteúdo2"},...')
    numeros_telefone = models.CharField(blank=True, max_length=50, help_text='Ex: (12) 98765 4321 (São permitidos múltiplos números)')
    email_contato = models.EmailField(blank=True, help_text='Ex: nome@empresa.com.br')
    endereco = models.CharField(blank=True, max_length=100, help_text="Ex: Rua Duque de Caxias, 237")
    cidade = models.CharField(max_length=50)
    horario_atendimento = models.CharField(blank=True, max_length=100, help_text='Ex: Seg à Sex das 10h as 17h.')
    # Links (usando URLField)
    link_loja = models.TextField(max_length=150, blank=True, help_text='Nome do botão e link para para site externo. Dict no formato {"Conheça nossa Loja Virtual":"https://minhaloja.com.br" }')
    reviews_link = models.URLField(blank=True, help_text="Link obtido abrindo o google empresas e clicando em Share > Send a link. Ex: https://maps.app.goo.gl/pTZvag2fg7ytV74eA")
    gmaps_link = models.CharField(blank=True, max_length=500, help_text="Link obtido abrindo o google empresas e clicando em Share > Embed a map > Small.")
    def __str__(self):
        return self.url

