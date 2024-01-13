from django.shortcuts import render
from django.views import View
#from .models import PageViewsCounter

# Create your views here.
class BaseLandPage(View):
    template_name = 'base_template.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.contador_model = None
        self.contador_key = None
        """    
        def get_contagem(self):
        contador, created = PageViewsCounter.objects.get_or_create(key=self.contador_key)
        contador.increment()
        self.context['contador_visitas'] = contador.value"""
             
    def get(self, request, *args, **kwargs):
        #self.get_contagem()
        return render(request, self.template_name, self.context)

class CatalogoDigital(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador_key = 'catalogo_digital'
        self.context = {
            'description' : 'Desenvolvimento de landing page para negócios, marketing e divulgação organica',
            'window_title': 'Catálogo Digital - Seu negócio na Web',
            'static_assets_path': 'cities/florianopolis/catalogodigital/assets',
            'sobretitulo': 'Bem Vindo ao Catálogo Digital!',
            'titulo': 'A melhor landing page para o seu negócio',
            'body_title': 'O que é uma landing page?',
            'body_subtitle': 'Uma landing page é como a vitrine virtual do seu negócio. É uma página da web criada sob medida para você. Imagine-a como a porta de entrada direta para o que sua empresa oferece de melhor. Permita que seus clientes o encontrem com os nossos serviços.',
            'item1_title': 'Presença Online',
            'item1_content': 'Oferecemos um serviço especializado com mais de 20 anos de experiência. Serviço reconhecido por nossos amigos e clientes.',
            'item2_title': 'Credibilidade',
            'item2_content': 'Com um design profissional e informações claras, transmitimos confiança, destacando sua marca de maneira sólida e confiável.',
            'item3_title': 'Publicidade Orgânica',
            'item3_content': 'Ao utilizar nossa plataforma, cada usuário é estimulado a explorar e conhecer outros empreendimentos na mesma área, promovendo uma rede colaborativa que amplia a visibilidade de todos. Assim, seu crescimento não é apenas individual, mas contribui para fortalecer e promover a prosperidade local.',
            'promocao_titulo': 'Aproveite nosso desconto exclusivo de lançamento!',
            'promocao_content': 'Informe que nos encontrou através do nosso site e ganhe 10% de desconto no valor da sua primeira anuidade!',
            'horario_atendimento': 'Seg à Sex das 07-19h.',
            'telefones': '(48) 996810518',
            'endereco': 'Rua Duque de Caxias, 634, Centenário, Sapiranga, RS',
            'whatslink': 'https://wa.me/+5551996810518',
            'gmaps_embed_link': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3468.0310528904797!2d-51.01371158831997!3d-29.631841339516633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95193fbe62929801%3A0xfb885bf48d7148d6!2sAJR%20Cutelaria!5e0!3m2!1sen!2sbr!4v1703100728491!5m2!1sen!2sbr',
        }

class AJRCutelaria(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador_key = 'ajr_cutelaria'
        self.context = {
            'description' : 'Landing page comercio local afiação amolador alicates de unha tesouras facas.',
            'window_title': 'Adelcio Afiador - Afiação e Venda de Ferramentas para Salões de beleza',
            'static_assets_path': 'cities/sapiranga/ajrcutelaria/assets',
            'sobretitulo': 'Afiação e Venda de Ferramentas para Salões de beleza',
            'titulo': 'Adélcio Amolador',
            'item1_title': 'Nossa História',
            'item1_content': 'Oferecemos um serviço especializado com mais de 20 anos de experiência. Serviço reconhecido por nossos amigos e clientes.',
            'item2_title': 'Produtos e Serviços',
            'item2_content': 'Serviço especializado de afiação para alicates, tesouras, facas e outras ferramentas profissionais. Temos também uma loja de ferramentas profissionais, incluindo espatulas de cutícula de alta qualidade e uma variedade de acessórios de reposição, de molas metálicas a borrachas de silicone para alicates.',
            'item3_title': 'Nosso Diferencial',
            'item3_content': 'Oferecemos não apenas serviços e produtos de qualidade, mas também comodidade, pois disponibilizamos atendimento personalizado no seu local de preferência, seja presencial ou remoto. Renove suas ferramentas com praticidade, sem sair do seu espaço de trabalho. Agende uma visita.',
            'promocao_titulo': 'Aproveite nosso desconto exclusivo!',
            'promocao_content': 'Informe que conheceu o nosso local através do nosso site e ganhe 10% de desconto no valor total da sua primeira compra! (Limitado à R$20)',
            'horario_atendimento': 'Seg à Sex das 07-19h.',
            'telefones': '(51) 980159178',
            'endereco': 'Rua Duque de Caxias, 634, Centenário, Sapiranga, RS',
            'whatslink': 'https://wa.me/+5551980159178',
            'gmaps_embed_link': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3468.0310528904797!2d-51.01371158831997!3d-29.631841339516633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95193fbe62929801%3A0xfb885bf48d7148d6!2sAJR%20Cutelaria!5e0!3m2!1sen!2sbr!4v1703100728491!5m2!1sen!2sbr',
        }

