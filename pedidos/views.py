from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def hello_world(request):
    return HttpResponse("Você está na raiz do subdominio pedidos.")

class BaseCardapioSimples(View):
    template_name = 'cardapio_simples.html'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
