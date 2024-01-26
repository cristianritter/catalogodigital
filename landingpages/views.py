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

def render_especial_subdomain(request):
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
        if not self.context:
            return HttpResponse("Os dados solicitados ainda não se encontram no banco de dados. Aguarde ou entre em contato com o administrador.")
        visitas = 1 + self.get_contagem()
        self.set_contagem(visitas)
        self.context['contador_visitas'] = visitas
        pares_colunas=zip(self.context['colunas_items'][::2], self.context['colunas_items'][1::2])  ##forma pares para apresentacao no template
        self.context['pares_colunas'] = pares_colunas
        return render(request, self.template_name, self.context)

  

class Homepage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render(request, 'portal.html')

class DemoView(BaseLandPage):
    def __init__(self, *args, **kwargs):
        url_cadastrada = 'demonstracao'
        super().__init__(*args, **kwargs)
        landing_page_data = LandingPageData.objects.filter(url_cadastrado=url_cadastrada).first()
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

class SejaNossoCliente(BaseLandPage):
    def __init__(self, *args, **kwargs):
        url_cadastrada = 'seja_nosso_cliente'
        super().__init__(*args, **kwargs)
        landing_page_data = LandingPageData.objects.filter(url_cadastrado=url_cadastrada).first()
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

class AJRCutelaria(BaseLandPage):
    def __init__(self, *args, **kwargs):
        url_cadastrada = 'ajr_cutelaria'
        super().__init__(*args, **kwargs)
        landing_page_data = LandingPageData.objects.filter(url_cadastrado=url_cadastrada).first()
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
          