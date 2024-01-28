from .models import LandingPageData
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def set_visitas(request):
    # Obter o valor do argumento 'visitas' da URL
    visitas_argumento = int(request.GET.get('visitas', 0))

    # Definir o novo valor da contagem de visitas
    cache.set('pagina_visitas', str(visitas_argumento), timeout=None)

    return HttpResponse(f'Contagem de visitas definida para {visitas_argumento}.')

class DefaultLandingPage(View):
    template_name = 'landing_page.html'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}
             
    def get_contagem(self):
        minha_pagina_visitas = cache.get('pagina_visitas')
        return int(minha_pagina_visitas) if minha_pagina_visitas else 0

    def set_contagem(self, minha_pagina_visitas):
        cache.set('pagina_visitas', str(minha_pagina_visitas), timeout=None)
      
    def get(self, request, *args, **kwargs):
        url_recebida = request.path.replace('/','')
        if not url_recebida: 
            url_recebida = 'seja_nosso_cliente'
        landing_page_data = LandingPageData.objects.filter(url_cadastrado=url_recebida).first()
        if landing_page_data and landing_page_data.on_air:
            self.context = {
                'endereco_bucket': landing_page_data.endereco_bucket+url_recebida+'/',
                'nomes_arquivos_imagens': landing_page_data.nomes_arquivos_imagens.replace('\r\n','').split(','),
                'nome_empresa': landing_page_data.nome_empresa,
                'descricao_curta': landing_page_data.descricao_curta,
                'meta_description': landing_page_data.meta_description,
                'lista_titulo': landing_page_data.lista_titulo,
                'lista_items': landing_page_data.lista_items.split('#'),  # Convertendo a string em uma lista
                'colunas_items': landing_page_data.colunas_items.split('#'),
                'numeros_telefone': landing_page_data.numeros_telefone,
                'email_contato': landing_page_data.email_contato,
                'endereco': landing_page_data.endereco,
                'horario_atendimento': landing_page_data.horario_atendimento,
                'whats_link': landing_page_data.whats_link,
                'reviews_link': landing_page_data.reviews_link,
                'gmaps_link': landing_page_data.gmaps_link,
                'link_loja': landing_page_data.link_loja,
            } 
        else:
            return render(request, '404-wall-e.html')  
        visitas = 1 + self.get_contagem()
        self.set_contagem(visitas)
        self.context['contador_visitas'] = visitas
        pares_colunas=zip(self.context['colunas_items'][::2], self.context['colunas_items'][1::2])  ##forma pares para apresentacao no template
        self.context['pares_colunas'] = pares_colunas
        return render(request, self.template_name, self.context)

class Homepage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render(request, 'portal.html')

