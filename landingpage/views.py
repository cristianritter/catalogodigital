from os import getenv

from django.http import HttpResponse
from .models import LandingPage
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.contrib.sitemaps import Sitemap
import ujson as json
from django.db.models import Q

BUCKET_ADDRESS = getenv('STORAGE_BUCKET')

class LandingPageView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'landing_page.html'

    def get(self, request, *args, **kwargs):
        url = request.path[1:] #/cidade/pagina
        data = cache.get(f'{url}.landing')
        if not data:
            print('entrou')
            data = LandingPage.objects.filter(url=url).first()
            if data:
                cache.set(f'{url}.landing', data, timeout=None)  
        if data and data.on_air:
            cidades = data.cidades.all().values_list('nome', flat=True)
            if data.colunas_items:
                colunas_items = json.loads(data.colunas_items)
            else:
                colunas_items = ''
                    
            self.context = {
                'endereco_bucket': BUCKET_ADDRESS+url.split('/')[1]+'/',
                'num_img_carousel': list(range(2, data.carousel_size+2)),
                'nome_empresa': data.nome_empresa,
                'descricao_curta': data.descricao_curta,
                'categoria': data.categoria_servico,
                'cidade': cidades,
                'lista_items': data.lista_items.splitlines(),
                'dados_dict': colunas_items,
                'numeros_telefone': data.numeros_telefone,
                'email_contato': data.email_contato,
                'endereco': data.endereco.split(','),
                'horario_atendimento': data.horario_atendimento,
                'link_whats': data.link_whats,
                'link_instagram': data.link_instagram,
                'link_facebook': data.link_facebook,
                'reviews_link': data.reviews_link,
                'gmaps_link': data.gmaps_link,
                'link_loja': data.link_loja.split('#'),
                'category': None,
                'company_name': None,
                'tagline': None,
                'address': None,
                'phone_numbers': None,
                'is_whatsapp': True,
                'e_mails': None,
                'social_media_links': None,
                'opening_hours': None,
            } 
        else:
            return render(request, '404-wall-e.html')  
        return render(request, self.template_name, self.context)

class Homepage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Obtém os dados do formulário, se existirem
        o_que = request.GET.get('q', '')
        onde = request.GET.get('local', '')
        resultados_busca = []
        q_placeholder = "Ex. afiador, cutelaria"
        if o_que or onde:
            q_placeholder = o_que
            result = LandingPage.objects.filter(
                Q(nome_empresa__icontains=o_que) |
                Q(categoria_servico__nome__icontains=o_que) |
                Q(trend_words__icontains=o_que),
                on_air=True
            ).order_by('-id')[:10]
            if result:
                for negocio in result:
                    resultados_busca.append(
                        {'nome_empresa': negocio.nome_empresa, 
                        'categoria': negocio.categoria_servico, 
                        'cidades': ', '.join(list(negocio.cidades.values_list('nome', flat=True))),
                        'url': negocio.url}
                    )
            else:
                resultados_busca = "nothing"

        # Contexto para enviar para o template
        self.context = {
            'resultados_busca': resultados_busca,
            'q_placeholder': q_placeholder
        }

        # Renderiza o template com os dados atualizados
        return render(request, 'home.html', self.context)

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

def favicon_view(request):
    # Lógica para ler e retornar o conteúdo do arquivo favicon.ico
    with open('landingpage/static/home/logo/favicon.ico', 'rb') as f:
        favicon = f.read()
    return HttpResponse(favicon, content_type='image/x-icon')