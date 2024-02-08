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
    descricao_curta = models.CharField(max_length=100, help_text='Resuma em uma sentença curta o que a empresa faz')
    lista_items = models.TextField(blank=True, help_text='Itens da lista em formato de list ["abc", "cde"]')
    colunas_items = models.TextField(blank=True, help_text='Conteúdo adicional no formato de dict. {"key": "value", "key2": "value2"}')
    numeros_telefone = models.CharField(blank=True, max_length=50, help_text='Números de telefone no formato (12) 98765 4321')
    email_contato = models.EmailField(blank=True, help_text='Email da empresa, se houver')
    endereco = models.CharField(blank=True, max_length=100, help_text="Endereço ou região da ede da empresa")
    horario_atendimento = models.CharField(blank=True, max_length=100, help_text='Horário de funcionamento')
    # Links (usando URLField)
    link_loja = models.URLField(blank=True, help_text="Link para loja virtual")
    reviews_link = models.URLField(blank=True, help_text="Link para os reviews do google")
    gmaps_link = models.URLField(blank=True, max_length=500, help_text="Link para os mapas 'embedded' no formato 'https:\\....br' ")
    def __str__(self):
        return self.url

