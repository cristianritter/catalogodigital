from django.core.cache import cache
from subdomains.utils import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.sitemaps import Sitemap
from .models import Store, Hub, Empresa
import json
from os import getenv
from landingpage.utils import Generate

BUCKET_ADDRESS = getenv('STORAGE_BUCKET')

def home(request):
    return redirect(reverse('DefaultLandingPage', subdomain=None))

class LojaView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'store.html'     
        
    def get(self, request, url, *args, **kwargs):
        print(request.path)
        url = request.path[1:].split('/')[-1]
        empresa = Empresa.objects.filter(name__iexact=url.replace('-', ' ')).first()
        loja__data = Store.objects.filter(empresa=empresa).first()
        if loja__data and loja__data.on_air:
            social_media = Generate._generate_social_links(loja__data.empresa.social_media)
            is_whats = True
            self.context = {
                'bucket': BUCKET_ADDRESS+request.path[1:]+'/store',
                'nome_empresa': loja__data.empresa.name,
                'link_whats': Generate._generate_whats_number(loja__data.empresa.phone_numbers, is_whats),
                'slogam': loja__data.empresa.tagline,
                'titulo': loja__data.titulo,
                'paragrafo': loja__data.paragrafo,
                'produtos': json.loads(loja__data.produtos),
                'social_media': social_media,
            } 
        else:
            return render(request, '404-wall-e.html')  
        return render(request, self.template_name, self.context)

class HubView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'hub.html'    
        self.portfolio_items = [
            {
                'link': 'https://loja.conectapages.com/japa',
                'image': 'common/hub/img/1.jpg',
                'heading': 'Threads',
                'subheading': 'Illustration'
            },
            {
                'link': '#portfolioModal2',
                'image': 'assets/img/portfolio/2.jpg',
                'heading': 'Explore',
                'subheading': 'Graphic Design'
            },
            # Adicione outros itens do portfólio conforme necessário
        ] 
    def get(self, request, url, *args, **kwargs):
        hub__data = Hub.objects.filter(url=(request.path).replace('/hub','')).first()
        if hub__data and hub__data.on_air:
            portfolio_items = []
            for item in hub__data.lojas.all():
                loja = {}
                url = Generate._generate_company_path(item.empresa.name, item.empresa.address)
                print(url)
                loja['url'] = f'https://loja.conectapages.com/{url}'
                loja['imagem'] = f'{BUCKET_ADDRESS}{url}/0.webp'
                loja['heading'] = item.empresa.name
                loja['subheading'] = item.empresa.tagline
                portfolio_items.append(loja)

            self.context = {
                #'endereco_bucket': loja__data.endereco_bucket+url+'/store/',
                #'nome_empresa': loja__data.nome_empresa,
                'nome': hub__data.empresa.name,
                'slogam': hub__data.empresa.tagline,
                'portfolio_items': portfolio_items,
            } 
        else:
            return render(request, '404-wall-e.html')  
        return render(request, self.template_name, self.context)

class LojaSitemap(Sitemap):
    changefreq = 'weekly'

    def _urls(self, page, protocol, domain):
        return super(LojaSitemap, self)._urls(
            page=page, protocol='https', domain='loja.conectapages.com')

    def items(self):
        urls = ['/']  # Esta é a URL da página inicial
        urls += ['/'+obj.url for obj in Store.objects.filter(on_air=True)]
        return urls
    
    def location(self, item):
        return item

    def priority(self, item):
        if item == '/':
            return 0.8  
        else:
            return 0.6  

