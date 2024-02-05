from django.core.cache import cache
from subdomains.utils import reverse
from django.shortcuts import redirect, render
from django.views import View
from .models import Loja
import json

def home(request):
    return redirect(reverse('DefaultLandingPage', subdomain=None))

class LojaView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'store.html'     
         
    def get(self, request, pagina, *args, **kwargs):
        loja__data = Loja.objects.filter(url_cadastrado=pagina[:-1:]).first()
        if loja__data and loja__data.on_air:
            self.context = {
                'meta_description': loja__data.meta_description,
                'endereco_bucket': loja__data.endereco_bucket+pagina+'store/',
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
        visitas = 1 + cache.get('visitas_lojas')
        cache.set('visitas_lojas', visitas, timeout=None)
        self.context['contador_visitas'] = visitas
        return render(request, self.template_name, self.context)

class HubView(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
        self.template_name = 'hub.html'     
        if not cache.get('contador_lj'):
            cache.set('contador_lj', 0, timeout=None)
         
    def get(self, request, pagina, *args, **kwargs):
        print('hub', pagina)
        loja__data = Loja.objects.filter(url_cadastrado=pagina).first()
        if loja__data and loja__data.on_air:
            self.context = {
                'meta_description': loja__data.meta_description,
                'endereco_bucket': loja__data.endereco_bucket+pagina+'/store/',
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
        visitas = 1 + cache.get('contador_lj')
        cache.set('contador_lj', visitas, timeout=None)
        self.context['contador_visitas'] = visitas
        return render(request, self.template_name, self.context)
