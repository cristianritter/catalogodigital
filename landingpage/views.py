from .models import LandingPage
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
import json

def set_visitas(request):
    visitas_argumento = int(request.GET.get('visitas', 0))
    cache.set('pagina_visitas', str(visitas_argumento), timeout=None)
    return HttpResponse(f'Contagem de visitas definida para {visitas_argumento}.')

class DefaultLandingPage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'new_landing_page.html'
        if not cache.get('contador_lp'):
            cache.set('contador_lp', 0, timeout=None)
      
    def get(self, request, *args, **kwargs):
        url_recebida = request.path.replace('/','')
        print(url_recebida)
        if not url_recebida: 
            url_recebida = 'seja_nosso_cliente'
        data = cache.get(f'{url_recebida}.landing')
        if not data:
            cache.set(f'{url_recebida}.landing', 0, timeout=60*2)
        landing_page_data = LandingPage.objects.filter(url_cadastrado=url_recebida).first()
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
                'endereco_bucket': landing_page_data.endereco_bucket+url_recebida+'/',
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
        visitas = 1 + cache.get('contador_lp')
        cache.set('contador_lp', visitas, timeout=None)
        self.context['contador_visitas'] = visitas
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

class NewLandingPage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'new_landing_page.html'
        self.landing_page_data = LandingPage.objects.filter(url_cadastrado='ajr_cutelaria').first()
      
    def get(self, request, *args, **kwargs):
        url_recebida='ajr_cutelaria'
        if self.landing_page_data and self.landing_page_data.on_air:
            try:
                lista_items = json.loads(self.landing_page_data.lista_items)
            except:
                return HttpResponse("AVISO: Revise a construção da seção 'Lista items' na página de administração.")
            try:
                dados_dict = json.loads(self.landing_page_data.colunas_items)
            except:
                return HttpResponse("AVISO: Revise a construção da seção 'Coluna items' na página de administração.")
           
            self.context = {
                'endereco_bucket': self.landing_page_data.endereco_bucket+url_recebida+'/',
                'nomes_arquivos_imagens': self.landing_page_data.nomes_arquivos_imagens.split(','),
                'nome_empresa': self.landing_page_data.nome_empresa,
                'descricao_curta': self.landing_page_data.descricao_curta,
                'meta_description': self.landing_page_data.meta_description,
                'lista_titulo': self.landing_page_data.lista_titulo,
                'lista_items': lista_items,
                'dados_dict': dados_dict,
                'numeros_telefone': self.landing_page_data.numeros_telefone,
                'email_contato': self.landing_page_data.email_contato,
                'endereco': self.landing_page_data.endereco,
                'horario_atendimento': self.landing_page_data.horario_atendimento,
                'link_whats': self.landing_page_data.link_whats,
                'link_instagram': self.landing_page_data.link_instagram,
                'link_facebook': self.landing_page_data.link_facebook,
                'reviews_link': self.landing_page_data.reviews_link,
                'gmaps_link': self.landing_page_data.gmaps_link,
                'link_loja': self.landing_page_data.link_loja,
            } 
        else:
            return render(request, '404-wall-e.html')  
        visitas = 1 + cache.get('contador_lp')
        cache.set('contador_lp', visitas, timeout=None)
        self.context['contador_visitas'] = visitas
        return render(request, self.template_name, self.context)
