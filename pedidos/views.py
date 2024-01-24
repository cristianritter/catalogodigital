from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def hello_world(request):
    return HttpResponse("Você está na raiz do subdominio pedidos.")

class BaseCardapioSimples(View):
    template_name = 'cardapio_simples.html'     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = {
            'coluna1': [
                {
                    'title': 'Hamburguer da casa',
                    'description': 'TrÊs carnes especiais angus de 120g',
                    'price': '32,90',
                    'image': '01.jpg'
                },
                {
                    'title': 'Hamburguer Duplo',
                    'description': 'Duas carnes especiais angus de 120g',
                    'price': '22,90',
                    'image': '02.jpg'
                }, 
                {
                    'title': 'Hamburguer da casa',
                    'description': 'TrÊs carnes especiais angus de 120g',
                    'price': '32,90',
                    'image': '03.jpg'
                },
            ],
            'coluna2': [
                {
                    'title': 'Hamburguer da casa',
                    'description': 'TrÊs carnes especiais angus de 120g',
                    'price': '32,90',
                    'image': '04.jpg'
                },
                {
                    'title': 'Hamburguer Duplo',
                    'description': 'Duas carnes especiais angus de 120g',
                    'price': '22,90',
                    'image': '05.jpg'
                }, 
                {
                    'title': 'Hamburguer da casa',
                    'description': 'TrÊs carnes especiais angus de 120g',
                    'price': '32,90',
                    'image': '06.jpg'
                },
            ],
             'coluna3': [
                {
                    'title': 'Hamburguer da casa',
                    'description': 'TrÊs carnes especiais angus de 120g',
                    'price': '32,90',
                    'image': '07.jpg'
                },
                {
                    'title': 'Hamburguer Duplo',
                    'description': 'Duas carnes especiais angus de 120g',
                    'price': '22,90',
                    'image': '08.jpg'
                }, 
                {
                    'title': 'Hamburguer da casa',
                    'description': 'TrÊs carnes especiais angus de 120g',
                    'price': '32,90',
                    'image': '03.jpg'
                },
            ]
        }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
