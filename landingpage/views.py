from django.http import HttpResponse
from .models import LandingPage
#from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.contrib.sitemaps import Sitemap
import ujson as json
from django.db.models import Q
from landingpage.utils import Generate, Storage

BUCKET_URL = Storage.get_bucket_url('')[:-1]

class LandingPageView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'landing_page.html'

    def get(self, request, *args, **kwargs):
        landingpage_data = LandingPage.objects.select_related('empresa').filter(url=request.path).first()
        print(request.path, landingpage_data)
        if not landingpage_data or not landingpage_data.on_air:
            return render(request, '404-wall-e.html') 
        
        self.context = {
            'bucket': (BUCKET_URL+'/landingpages/' + str(landingpage_data.id) +'/'),
            'img_carousel': list(range(2, landingpage_data.carousel_size+2)),
            'company_name': landingpage_data.empresa.name,
            'tagline': landingpage_data.empresa.tagline,
            'category': landingpage_data.empresa.category,
            'address': landingpage_data.empresa.address.split(','),
            'phone_numbers': landingpage_data.empresa.phone_numbers,
            'lista_items': landingpage_data.lista_items.splitlines(),
            'heading_style': landingpage_data.heading_style,   
        }
        
        if (landingpage_data.empresa.social_media):
            print('social media entrou')
            self.context['social_media'] = Generate._generate_social_links(landingpage_data.empresa.social_media)
        
        if landingpage_data.empresa.service_areas:
            self.context['service_areas'] = landingpage_data.empresa.service_areas.all().values_list('nome', flat=True)
        
        if landingpage_data.colunas_items:
            self.context['dados_dict'] = json.loads(landingpage_data.colunas_items)
        
        if landingpage_data.empresa.is_whatsapp:
            self.context['whats_number'] = Generate._generate_whats_number(landingpage_data.empresa.phone_numbers.split(',')[0])

        if landingpage_data.empresa.e_mail:
            self.context['e_mail'] = landingpage_data.empresa.e_mail
        
        if landingpage_data.empresa.opening_hours:
            self.context['opening_hours'] = landingpage_data.empresa.opening_hours
        
        if landingpage_data.empresa.website:
            self.context['link_loja'] = landingpage_data.empresa.website.split('#')
        
        if landingpage_data.empresa.g_embbedmaps:
            self.context['gmaps_link'] = landingpage_data.empresa.g_embbedmaps
        
        if landingpage_data.empresa.g_business:
            self.context['reviews_link'] = landingpage_data.empresa.g_business

        return render(request, self.template_name, self.context)

class Homepage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Obtém os dados do formulário, se existirem
        o_que = request.GET.get('q', '')
        onde = request.GET.get('local', '')
        resultados_busca = []
        q_placeholder = "Ex. afiador, advogado"
        if o_que or onde:
            q_placeholder = o_que
            search_slicing = int(len(o_que)/2)+1
            result = LandingPage.objects.filter(
                Q(empresa__name__icontains=o_que) |
                Q(empresa__category__name__icontains=o_que[:search_slicing]),
                on_air=True
            ).order_by('-id')[:10]
            if result:
                for landingpage in result:
                    resultados_busca.append(
                        {'nome_empresa': landingpage.empresa.name, 
                        'categoria': landingpage.empresa.category, 
                        'cidades': ', '.join(list(landingpage.empresa.service_areas.values_list('nome', flat=True))),
                        'url': Generate._generate_company_path(landingpage.empresa.name, landingpage.empresa.address)}
                    )
            else:
                resultados_busca = "nothing"

        self.context = {
            'resultados_busca': resultados_busca,
            'q_placeholder': q_placeholder
        }

        return render(request, 'home.html', self.context)

class RootSitemap(Sitemap):
    changefreq = 'weekly'

    def _urls(self, page, protocol, domain):
        return super(RootSitemap, self)._urls(
            page=page, protocol='https', domain='www.conectapages.com')

    def items(self):
        urls = ['/']  # Esta é a URL da página inicial
        urls += ['/'+Generate._generate_company_path(obj.empresa.name, obj.empresa.address) for obj in LandingPage.objects.filter(on_air=True)]
        return urls
    
    def location(self, item):
        return item

    def priority(self, item):
        if item == '/':
            return 1.0  
        else:
            return 0.7  

def favicon_view(request):
    print('buscando favicon')
    # Lógica para ler e retornar o conteúdo do arquivo favicon.ico
    with open('landingpage/static/common/favicon/favicon-128x128.png', 'rb') as f:
        favicon = f.read()
    return HttpResponse(favicon, content_type='image/png')