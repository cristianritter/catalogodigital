from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from .models import LojaData
import json

def redirect_to_landingpage(request):
    # Redireciona para a URL de landingpage
    return redirect('landingpages:seja_nosso_cliente')

class BaseLoja(View):
    template_name = 'store.html'     
    def __init__(self, *args, **kwargs):
        url_cadastrada = 'cardapio_simples'
        super().__init__(*args, **kwargs)
        loja__data = LojaData.objects.filter(url_cadastrado=url_cadastrada).first()
        self.context = {
            'meta_description': loja__data.meta_description,
            'caminho_arquivos': loja__data.caminho_de_arquivos,
            'nome_empresa': loja__data.nome_empresa,
            'slogam': loja__data.slogam,
            'titulo': loja__data.titulo,
            'paragrafo': loja__data.paragrafo,
            'link_whats': loja__data.link_whats,
            'link_instagram': loja__data.link_instagram,
            'link_facebook': loja__data.link_facebook,
            'produtos': json.loads(loja__data.produtos.lower()),
        }
        print(self.context['produtos'])
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
