from django.http import HttpResponse
from .models import Empresa, LandingPage
#from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.contrib.sitemaps import Sitemap
import ujson as json
from django.db.models import Q
from landingpage.utils import Generate, Storage

BUCKET_URL = Storage.get_bucket_url('')

class LandingPageView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'landing_page.html'

    def get(self, request, *args, **kwargs):
        url:list = request.path[1:].split('/')[-1]
        empresa = Empresa.objects.filter(name__iexact=url.replace('-', ' ')).first()
        data = LandingPage.objects.filter(empresa=empresa).first()
        if data and data.on_air:
            social_media = Generate._generate_social_links(data.empresa.social_media)
            service_areas = data.empresa.service_areas.all().values_list('nome', flat=True)
            if data.colunas_items:
                colunas_items = json.loads(data.colunas_items)
            else:
                colunas_items = ''
            is_whats = True
            self.context = {
                'bucket': BUCKET_URL+url+'/',
                'img_carousel': list(range(2, data.carousel_size+2)),
                'nome_empresa': data.empresa.name,
                'category': data.empresa.category,
                'service_areas': service_areas,
                'address': data.empresa.address.split(','),
                'opening_hours': data.empresa.opening_hours,
                'phone_numbers': data.empresa.phone_numbers,
                'whats_number': Generate._generate_whats_number(data.empresa.phone_numbers, is_whats),
                'e_mail': data.empresa.e_mail,
                'social_media': social_media,
                'lista_items': data.lista_items.splitlines(),
                'dados_dict': colunas_items,
                'reviews_link': data.empresa.g_business,
                'gmaps_link': data.empresa.g_embbedmaps,
                'link_loja': data.empresa.website.split('#'),
                'company_name': data.empresa.name,
                'tagline': data.empresa.tagline,
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

        self.context = {
            'resultados_busca': resultados_busca,
            'q_placeholder': q_placeholder
        }

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