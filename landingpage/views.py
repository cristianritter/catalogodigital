from .models import LandingPage
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.contrib.sitemaps import Sitemap
from django.utils.text import slugify
import json

class DefaultLandingPage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'landing_page.html'

    def get(self, request, *args, **kwargs):
        parametros_da_url = request.path.split('/') #cidade, nome-da-pagina
        url = parametros_da_url[-1]
        cidade = parametros_da_url[-2]
        data = cache.get(f'{url}.landing')
        if not data:
            data = LandingPage.objects.filter(url=url).first()
            if data:
                cache.set(f'{url}.landing', data, timeout=None)    
    
        if data and data.on_air:
            if not cidade:
                cidade = str(data.cidades.first()).lower()
            if data.link_loja:
                link_loja = json.loads(data.link_loja)
            else:
                link_loja = ''
            if data.lista_items:
                lista_items = json.loads(data.lista_items)
            else:
                lista_items = ''
            if data.colunas_items:
                colunas_items = json.loads(data.colunas_items)
            else:
                colunas_items = ''
                    
            self.context = {
                'endereco_bucket': cache.get('file_bucket_address')+url+'/',
                'num_img_carousel': list(range(2, data.carousel_size+2)),
                'nome_empresa': data.nome_empresa,
                'descricao_curta': data.descricao_curta,
                'categoria': data.categoria_servico,
                'cidade': data.cidades.filter(nome__icontains=cidade).first(),
                'trend_words': data.trend_words,
                'lista_items': lista_items,
                'dados_dict': colunas_items,
                'numeros_telefone': data.numeros_telefone,
                'email_contato': data.email_contato,
                'endereco': data.endereco,
                'horario_atendimento': data.horario_atendimento,
                'link_whats': data.link_whats,
                'link_instagram': data.link_instagram,
                'link_facebook': data.link_facebook,
                'reviews_link': data.reviews_link,
                'gmaps_link': data.gmaps_link,
                'link_loja': link_loja,
            } 
        else:
            return render(request, '404-wall-e.html')  
        return render(request, self.template_name, self.context)

class Homepage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        self.context = {
            'empresas': [
                {'nome_empresa': 'Adelcio-afiador',
                'url': 'conectapages.com/adelcio-afiador'}
            ]
        }
        return render(request, 'home.html', self.context)

class RootSitemap(Sitemap):
    changefreq = 'daily'

    def _urls(self, page, protocol, domain):
        return super(RootSitemap, self)._urls(
            page=page, protocol='https', domain='conectapages.com')

    def items(self):
        urls = ['/']  # Esta é a URL da página inicial
        for item in LandingPage.objects.filter(on_air=True):
            print(item)
            for cidade in item.cidades.all():
                cidade = str(cidade).split('-')[0]
                urls += [f'/{slugify(cidade)}/{item.url}']
        #urls += ['/'+obj.url for obj in LandingPage.objects.filter(on_air=True)]
        return urls
    
    def location(self, item):
        return item

    def priority(self, item):
        if item == '/':
            return 1.0  
        else:
            return 0.7  

