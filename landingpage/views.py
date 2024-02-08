from .models import LandingPage
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
import json
from django.conf import settings

from os import getenv

def update_cache(request, url=""):
    if url:
        resposta = f"O endereço {url} foi atualizado."
        cache.delete(f'{url}.landing')
    else:
        resposta = f"Todo conteúdo da cache foi apagado."
        cache.clear()
    cache.set('file_bucket_address', getenv('STORAGE_BUCKET'), timeout=None)
    cache.set('seja_nosso_cliente.landing', LandingPage.objects.get(url='seja_nosso_cliente'), timeout=60*60*24*7)
    return HttpResponse('Cache cleared!!!'+resposta)    

class DefaultLandingPage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'landing_page.html'
       
        cache.set('file_bucket_address', getenv('STORAGE_BUCKET'), timeout=None)
        cache.set('seja_nosso_cliente.landing', LandingPage.objects.get(url='seja_nosso_cliente'), timeout=60*60*24*7)
   
    def get(self, request, *args, **kwargs):
        url_recebida = request.path.replace('/','')
        if not url_recebida: 
            url_recebida = 'seja_nosso_cliente'
        if settings.IS_HEROKU_APP:
            data = cache.get(f'{url_recebida}.landing')
        else:
            data = None
        if not data:
            print('getting from posgtgres')
            data = LandingPage.objects.filter(url=url_recebida).first()
            if data and data.on_air:
                cache.set(f'{url_recebida}.landing', data, timeout=60*60*24)    
        if data:
            try:
                lista_items = json.loads(data.lista_items)
            except:
                lista_items = {}
            try:
                dados_dict = json.loads(data.colunas_items)
            except:
                dados_dict = {}           
            self.context = {
                'endereco_bucket': cache.get('file_bucket_address')+url_recebida+'/',
                'num_img_carousel': list(range(2, data.carousel_size+2)),
                'nome_empresa': data.nome_empresa,
                'descricao_curta': data.descricao_curta,
                'meta_description': data.meta_description,
                'lista_titulo': data.lista_titulo,
                'lista_items': lista_items,
                'dados_dict': dados_dict,
                'numeros_telefone': data.numeros_telefone,
                'email_contato': data.email_contato,
                'endereco': data.endereco,
                'horario_atendimento': data.horario_atendimento,
                'link_whats': data.link_whats,
                'link_instagram': data.link_instagram,
                'link_facebook': data.link_facebook,
                'reviews_link': data.reviews_link,
                'gmaps_link': data.gmaps_link,
                'link_loja': data.link_loja,
            } 
        else:
            return render(request, '404-wall-e.html')  
        return render(request, self.template_name, self.context)

class Homepage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render(request, 'portal.html')

class RootSitemap(Sitemap):
    changefreq = 'daily'

    def _urls(self, page, protocol, domain):
        return super(RootSitemap, self)._urls(
            page=page, protocol='https', domain='conectapages.com')

    def items(self):
        urls = ['/']  # Esta é a URL da página inicial
        urls += ['/'+obj.url for obj in LandingPage.objects.filter(on_air=True)]
        return urls
    
    def location(self, item):
        return item

    def priority(self, item):
        if item == '/':
            return 1.0  
        else:
            return 0.7  

