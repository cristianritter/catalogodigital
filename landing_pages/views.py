from .models import LandingPageData
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
EmpresasDivulgadas = list()

#from .models import PageViewsCounter

#@csrf_protect
@csrf_exempt
def set_demo_view(request):
    if request.method == 'POST':
        # Recebe o JSON do corpo da requisição
        try:
            data = json.loads(request.body.decode('utf-8'))
            #print('data',data)
            cache.set('demo_view_context',  data, timeout=None)
            print(cache.get('demo_view_context'))
            #print("JSON recebido:", data)
            return JsonResponse({'status': 'success', 'message': 'JSON recebido com sucesso'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Erro ao decodificar JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)

def render_root_page(request):
    subdomain = request.subdomain
    if str(subdomain).lower() == 'ajrcutelaria': 
        return AJRCutelaria.as_view()(request)
    else:
        return SejaNossoCliente.as_view()(request)

def set_visitas(request):
    # Obter o valor do argumento 'visitas' da URL
    visitas_argumento = int(request.GET.get('visitas', 0))

    # Definir o novo valor da contagem de visitas
    cache.set('pagina_visitas', str(visitas_argumento), timeout=None)

    return HttpResponse(f'Contagem de visitas definida para {visitas_argumento}.')

class BaseLandPage(View):
    template_name = 'landing_page.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
             
    def get_contagem(self):
        minha_pagina_visitas = cache.get('pagina_visitas')
        return int(minha_pagina_visitas) if minha_pagina_visitas else 0

    def set_contagem(self, minha_pagina_visitas):
        cache.set('pagina_visitas', str(minha_pagina_visitas), timeout=None)
      
    def get(self, request, *args, **kwargs):
        print(self.context)
        if not self.context:
            return HttpResponse("Os dados solicitados não se encontram no banco de dados.")
        visitas = 1 + self.get_contagem()
        self.set_contagem(visitas)
        self.context['contador_visitas'] = visitas
        return render(request, self.template_name, self.context)

class DemoView(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = cache.get('demo_view_context')
        print(self.context)

class Homepage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render(request, 'portal.html')

class SejaNossoCliente(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {
            'static_assets_path': 'cities/florianopolis/seja_nosso_cliente/assets',
            'carousel_counter': range(4),
            'meta_description' : 'Serviço de desenvolvimento e hospedagem de landing pages para negócios, marketing e divulgação organica',
            'window_title': 'MK4 Digital - Seu negócio na Web',
            'sobretitulo': 'Bem Vindo a MK4 Digital!',
            'titulo': 'A melhor landing page para o seu negócio',
            'body_title': 'O que é uma LANDING PAGE?',
            'lista_servicos': ['É a vitrine virtual do seu negócio', 
                               'Um cartão de visita na web feito sob medida para você', 
                               'Uma ponte entre você e o seu cliente', 
                                ],
            'item1_title': 'Presença Online',
            'item1_content': 'Torne-se conhecido deixando seus clientes saberem que você existe e a qualidade do seu serviço.',
            'item2_title': 'Credibilidade',
            'item2_content': 'Com um design profissional e informações claras, transmitimos confiança, destacando sua marca de maneira sólida e confiável.',
            'item3_title': 'Publicidade Orgânica',
            'item3_content': 'Ao utilizar nossa plataforma, cada usuário é estimulado a explorar e conhecer outros empreendimentos na mesma área, promovendo uma rede colaborativa que amplia a visibilidade de todos. Assim, seu crescimento não é apenas individual, mas contribui para fortalecer e promover a prosperidade local. (Nosso Portal está em desenvolvimento)',
            'promocao_content': 'Condições especiais para os primeiros assinantes!',
            'horario_atendimento': 'Seg à Sex das 07-19h.',
            'telefones': '(48) 996810518',
            'whatslink': 'https://wa.me/+5548996810518',
            'email':'mkquatrodigital@gmail.com', 
            'google_share_link': '',
            'endereco': '',
            'gmaps_embed_link': '',
        }

'''class KelliSenaAcessoria(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {
            'static_assets_path': 'cities/saopaulo/kellisenaassessoria/assets',
            'meta_description' : 'Landing page de Assessoria trabalhista e financeira em São Paulo no Alto do Ipiranga, atende todo o Brasil.',
            'window_title': 'Kelli Sena - Assessoria trabalhista e financeira',
            'sobretitulo': 'Assessoria trabalhista e financeira',
            'titulo': 'Kelli Sena',
            'body_title': 'teste1 ',
            'lista_servicos': ['Afiação de Alicates e Tesouras', 'Afiação de facas', 'Venda de Ferramentas', 'Atendimento à domicílio', 'Consulte as regiões de cobertura'],
            'item1_title': 'Nossa História',
            'item1_content': 'Serviço especializado com mais de 14 anos de experiência.',
            'item2_title': 'Serviços Oferecidos',
            'item2_content': 'Assessoria admissional, gozo de férias, cálculos recisórios e elaboração de folha de pagamento, encargos e obrigações assessórias.',
            'item3_title': 'Nosso Diferencial',
            'item3_content': 'Assessoria jurídica especializada com expertise legislativa, cálculos precisos e atendimento personalizado.',
            'promocao_content': 'Informe que conheceu o nosso local através do nosso site e ganhe 5% de desconto no valor total do seu primeiro serviço!5',
            'horario_atendimento': 'Seg à Sex das 09-17h.',
            'telefones': '(11) 95296-4549',
            'email':'', 
            'whatslink': 'https://wa.me/+5511952964549',
            'google_share_link': '',
            'endereco': '',
            'gmaps_embed_link': '',
        }'''
class AJRCutelaria(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        landing_page_data = LandingPageData.objects.filter(url_cadastrado='ajr_cutelaria').first()
        if landing_page_data:
            self.context = {
                'num_imagens_carrousel': range(landing_page_data.num_imagens_carrousel),
                'caminho_arquivos': landing_page_data.caminho_de_arquivos,
                'nome_empresa': landing_page_data.nome_empresa,
                'descricao_curta': landing_page_data.descricao_curta,
                'meta_description': landing_page_data.meta_description,
                'lista_titulo': landing_page_data.lista_titulo,
                'lista_items': landing_page_data.lista_items.split(','),  # Convertendo a string em uma lista
                'colunas_items': landing_page_data.colunas_items.split('#'),
                'numeros_telefone': landing_page_data.numeros_telefone,
                'email_contato': landing_page_data.email_contato,
                'endereco': landing_page_data.endereco,
                'horario_atendimento': landing_page_data.horario_atendimento,
                'whats_link': landing_page_data.whats_link,
                'reviews_link': landing_page_data.reviews_link,
                'gmaps_link': landing_page_data.gmaps_link,
            }
            pares_colunas=zip(self.context['colunas_items'][::2], self.context['colunas_items'][1::2])
            self.context['pares_colunas'] = pares_colunas
        
        """
            'caminho_arquivos': 'sapiranga/ajr_cutelaria',
            'caminho_arquivos': 'sapiranga/ajr_cutelaria',
            'num_imagens_carrousel': range(3),
            'meta_description' : 'Afiador e Amolador de Alicates de cutícula, tesouras e facas. Serviço e comercio local em Sapiranga, Rio Grande do Sul.',
            'descricao_curta': 'Afiação e Venda de Ferramentas para Salões de beleza',
            'nome_empresa': 'Adélcio Amolador',
            'lista_titulo': 'Produtos e Serviços',
            'lista_items': ['Afiação de Alicates e Tesouras', 'Afiação de facas', 'Venda de Ferramentas', 'Atendimento à domicílio', 'Consulte as regiões de cobertura'],
            'colunas_items': ['Nossa História', 'Oferecemos um serviço especializado com mais de 20 anos de experiência. Serviço reconhecido por nossos amigos e clientes.',
                'Tudo o que você precisa', 'Serviço especializado de afiação para alicates, tesouras, facas e outras ferramentas profissionais. Temos também uma loja de ferramentas profissionais, incluindo espatulas de cutícula de alta qualidade e uma variedade de acessórios de reposição, de molas metálicas a borrachas de silicone para alicates.',
                'Nosso Diferencial', 'Oferecemos não apenas serviços e produtos de qualidade, mas também comodidade, pois disponibilizamos atendimento personalizado no seu local de preferência, seja presencial ou remoto. Renove suas ferramentas com praticidade, sem sair do seu espaço de trabalho. Agende uma visita.',
                'Aproveite',  'Informe que conheceu a empresa através do site e ganhe 10% de desconto no valor total da sua primeira compra! (Limitado à R$10)',
            ],  
            'horario_atendimento': 'Seg à Sex das 07-19h.',
            'numeros_telefone': '(51) 980159178',
            'email_contato':'', 
            'whats_link': 'https://wa.me/+5551980159178',
            'reviews_link': 'https://maps.app.goo.gl/pTZvag2fg7ytV74eA',
            'endereco': 'Rua Duque de Caxias, 634, Centenário, Sapiranga, RS',
            'gmaps_link': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3468.0310528904797!2d-51.01371158831997!3d-29.631841339516633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95193fbe62929801%3A0xfb885bf48d7148d6!2sAJR%20Cutelaria!5e0!3m2!1sen!2sbr!4v1703100728491!5m2!1sen!2sbr',
            """        
 
class ResidencialVivaTorres(BaseLandPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        landing_page_data = LandingPageData.objects.filter(url_cadastrado='ajr_cutelaria').first()
        if landing_page_data:
            self.context = {
                'num_imagens_carrousel': range(landing_page_data.num_imagens_carrousel),
                'caminho_arquivos': landing_page_data.caminho_de_arquivos,
                'nome_empresa': landing_page_data.nome_empresa,
                'descricao_curta': landing_page_data.descricao_curta,
                'meta_description': landing_page_data.meta_description,
                'lista_titulo': landing_page_data.lista_titulo,
                'lista_items': landing_page_data.lista_items.split(','),  # Convertendo a string em uma lista
                'colunas_items': landing_page_data.colunas_items.split('#'),
                'numeros_telefone': landing_page_data.numeros_telefone,
                'email_contato': landing_page_data.email_contato,
                'endereco': landing_page_data.endereco,
                'horario_atendimento': landing_page_data.horario_atendimento,
                'whats_link': landing_page_data.whats_link,
                'reviews_link': landing_page_data.reviews_link,
                'gmaps_link': landing_page_data.gmaps_link,
            }
            pares_colunas=zip(self.context['colunas_items'][::2], self.context['colunas_items'][1::2])
            self.context['pares_colunas'] = pares_colunas
        