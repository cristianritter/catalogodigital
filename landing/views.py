from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


#from .models import PageViewsCounter
# Create your views here.

def set_visitas(request):
    # Obter o valor do argumento 'visitas' da URL
    visitas_argumento = int(request.GET.get('visitas', 0))

    # Definir o novo valor da contagem de visitas
    cache.set('pagina_visitas', str(visitas_argumento))

    return HttpResponse(f'Contagem de visitas definida para {visitas_argumento}.')

class ListaPedidos(View):
    template_name = 'lista_pedidos.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
      
    def get(self, request, *args, **kwargs):
        # Criando um contexto fictício para testar a aparência
        pedidos = [
            {
                'horario': '2024-01-16 10:30:00',
                'mesa': 1,
                'itens': 'Hamburguer, Batata Frita',
                'valor': 15.99,
                'status': 'Aguardando',
                'pago': False,
            },
            {
                'horario': '2024-01-16 11:45:00',
                'mesa': 2,
                'itens': 'Pizza, Refrigerante',
                'valor': 25.50,
                'status': 'Preparando',
                'pago': True,
            },
        # Adicione mais pedidos conforme necessário
        ]

        self.context = {'pedidos': pedidos}
        return render(request, self.template_name, self.context)

class BaseLandPage(View):
    template_name = 'base_template.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
             
    def get_contagem(self):
        minha_pagina_visitas = cache.get('pagina_visitas')
        return int(minha_pagina_visitas) if minha_pagina_visitas else 0

    def set_contagem(self, minha_pagina_visitas):
        cache.set('pagina_visitas', str(minha_pagina_visitas))
      
    def get(self, request, *args, **kwargs):
        visitas = 1 + self.get_contagem()
        self.set_contagem(visitas)
        self.context['contador_visitas'] = visitas
        return render(request, self.template_name, self.context)

class CatalogoDigital(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

class KelliSenaAcessoria(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {
            'description' : 'Landing page assessoria juridica atendimento em todo o pais, são paulo.',
            'window_title': 'Kelli Sena - Assessoria trabalhista e financeira',
            'static_assets_path': 'cities/saopaulo/kellisenaassessoria/assets',
            'sobretitulo': 'Assessoria trabalhista e financeira',
            'titulo': 'Kelli Sena',
            'item1_title': 'Nossa História',
            'item1_content': 'Serviço especializado com mais de 14 anos de experiência.',
            'item2_title': 'Serviços Oferecidos',
            'item2_content': 'Assessoria admissional, gozo de férias, cálculos recisórios e elaboração de folha de pagamento, encargos e obrigações assessórias.',
            'item3_title': 'Nosso Diferencial',
            'item3_content': 'Assessoria jurídica especializada com expertise legislativa, cálculos precisos e atendimento personalizado.',
            'promocao_titulo': 'Aproveite nosso desconto exclusivo!',
            'promocao_content': 'Informe que conheceu o nosso local através do nosso site e ganhe 5% de desconto no valor total da sua primeira compra! (Limitado à R$20)',
            'horario_atendimento': 'Seg à Sex das 09-17h.',
            'telefones': '(11) 95296-4549',
            'endereco': 'Alto Ipiranga, São Paulo, SP',
            'whatslink': 'https://wa.me/+5511952964549',
            'gmaps_embed_link': '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10341.049867764943!2d-46.62931362676512!3d-23.600271298884838!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce5ba9cdaeaf81%3A0x8cccb9a54c7a0280!2sIpiranga!5e0!3m2!1sen!2sbr!4v1705458908604!5m2!1sen!2sbr"></iframe>',
        }


class AJRCutelaria(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

class ResidencialVivaTorres(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {
            'description' : 'Landing page alugueis de temporada.',
            'window_title': 'Residencial VivaTorres - Alugueis de Temporada',
            'static_assets_path': 'cities/torres/residencialvivatorres/assets',
            'sobretitulo': 'Residencial Viva Torres',
            'titulo': 'Aluguéis de temporada',
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