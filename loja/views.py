from django.core.cache import cache
from subdomains.utils import reverse
from django.shortcuts import redirect, render
from django.views import View
from .models import Loja, Hub
import json

def home(request):
    return redirect(reverse('DefaultLandingPage', subdomain=None))

class LojaView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'store.html'     
         
    def get(self, request, url, *args, **kwargs):
        loja__data = Loja.objects.filter(url_cadastrado=url.replace('/','')).first()
        if loja__data and loja__data.on_air:
            self.context = {
                'meta_description': loja__data.meta_description,
                'endereco_bucket': loja__data.endereco_bucket+url+'/store',
                'nome_empresa': loja__data.nome_empresa,
                'link_whats': loja__data.link_whats,
                'link_facebook': loja__data.link_facebook,
                'link_instagram': loja__data.link_instagram,
                'slogam': loja__data.slogam,
                'titulo': loja__data.titulo,
                'paragrafo': loja__data.paragrafo,
                'produtos': json.loads(loja__data.produtos),
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
        hub__data = Hub.objects.filter(url=url.replace('/','')).first()
        if hub__data and hub__data.on_air:
            portfolio_items = []
            for item in hub__data.lojas.all():
                loja = {}
                print(item.url_cadastrado)
                loja['url'] = f'https://loja.conectapages.com/{item.url_cadastrado}'
                loja['imagem'] = f'{item.endereco_bucket}{item.url_cadastrado}/store/cover.webp'
                loja['heading'] = item.nome_empresa
                loja['subheading'] = item.slogam
                portfolio_items.append(loja)

            self.context = {
                'meta_description': hub__data.meta_description,
                #'endereco_bucket': loja__data.endereco_bucket+url+'/store/',
                #'nome_empresa': loja__data.nome_empresa,
                'nome': hub__data.nome,
                'slogam': hub__data.slogam,
                'portfolio_items': portfolio_items,
            } 
        else:
            return render(request, '404-wall-e.html')  
        return render(request, self.template_name, self.context)
