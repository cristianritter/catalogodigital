from .models import LandingPage, Sistema
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
import json

def update_cache(request, url):
    if url:
        resposta = cache.delete(f'{url}.landing')
    else:
        resposta = cache.clear()
    return HttpResponse('Cache cleared!!!', resposta)    

class DefaultLandingPage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'landing_page.html'
        cache.set('file_bucket_address',Sistema.objects.get(on_air=True).repositorio_imagens, timeout=None)
        cache.set('seja_nosso_cliente.landing', LandingPage.objects.get(url_cadastrado='seja_nosso_cliente'), timeout=60*60*24*7)

      
    def get(self, request, *args, **kwargs):
        url_recebida = request.path.replace('/','')
        if not url_recebida: 
            url_recebida = 'seja_nosso_cliente'
        data = cache.get(f'{url_recebida}.landing')
        if not data:
            cache.set(f'{url_recebida}.landing', 0, timeout=60*60*24)
        landing_page_data = LandingPage.objects.get(url_cadastrado=url_recebida)
        if landing_page_data and landing_page_data.on_air:
            try:
                lista_items = json.loads(landing_page_data.lista_items)
            except:
                return HttpResponse("AVISO: Revise a construção da seção 'Lista items' na página de administração.")
            try:
                dados_dict = json.loads(landing_page_data.colunas_items)
            except:
                return HttpResponse("AVISO: Revise a construção da seção 'Coluna items' na página de administração.")
           
            self.context = {
                'endereco_bucket': cache.get('file_bucket_address')+url_recebida+'/',
                'nomes_arquivos_imagens': landing_page_data.nomes_arquivos_imagens.split(','),
                'nome_empresa': landing_page_data.nome_empresa,
                'descricao_curta': landing_page_data.descricao_curta,
                'meta_description': landing_page_data.meta_description,
                'lista_titulo': landing_page_data.lista_titulo,
                'lista_items': lista_items,
                'dados_dict': dados_dict,
                'numeros_telefone': landing_page_data.numeros_telefone,
                'email_contato': landing_page_data.email_contato,
                'endereco': landing_page_data.endereco,
                'horario_atendimento': landing_page_data.horario_atendimento,
                'link_whats': landing_page_data.link_whats,
                'link_instagram': landing_page_data.link_instagram,
                'link_facebook': landing_page_data.link_facebook,
                'reviews_link': landing_page_data.reviews_link,
                'gmaps_link': landing_page_data.gmaps_link,
                'link_loja': landing_page_data.link_loja,
            } 
        else:
            return render(request, '404-wall-e.html')  
        return render(request, self.template_name, self.context)

class Homepage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render(request, 'portal.html')

class Sitemap(Sitemap):
    changefreq = 'weekly'

    def items(self):
        urls = ['/']  # Esta é a URL da página inicial
        urls += ['/'+obj.url_cadastrado for obj in LandingPage.objects.filter(on_air=True)]
        return urls
    
    def location(self, item):
        return item

    def priority(self, item):
        if item == '/':
            return 1.0  
        else:
            return 0.7  

