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
            'cardapio': {
                'pizza': [
                    {'title': 'Pizza Margherita', 'description': 'Delicious Margherita pizza.', 'price': 12.99, 'image': '01.jpg'},
                    {'title': 'Pizza Pepperoni', 'description': 'Spicy Pepperoni pizza.', 'price': 14.99, 'image': '02.jpg'},
                    {'title': 'Pizza Margherita', 'description': 'Delicious Margherita pizza.', 'price': 12.99, 'image': '01.jpg'},
                    {'title': 'Pizza Margherita', 'description': 'Delicious Margherita pizza.', 'price': 12.99, 'image': '01.jpg'},
                    {'title': 'Pizza Margherita', 'description': 'Delicious Margherita pizza.', 'price': 12.99, 'image': '01.jpg'},
                    # Adicione mais itens de pizza conforme necessário
                ],
                'salad': [
                    {'title': 'Caesar Salad', 'description': 'Fresh Caesar salad.', 'price': 8.99, 'image': '03.jpg'},
                    {'title': 'Caesar Salad', 'description': 'Fresh Caesar salad.', 'price': 8.99, 'image': '03.jpg'},
                    {'title': 'Greek Salad', 'description': 'Classic Greek salad.', 'price': 9.99, 'image': '04.jpg'},
                    # Adicione mais itens de salada conforme necessário
                ],
                'noodle': [
                    {'title': 'Spaghetti Bolognese', 'description': 'Hearty Bolognese spaghetti.', 'price': 10.99, 'image': '05.jpg'},
                    {'title': 'Pad Thai', 'description': 'Authentic Pad Thai.', 'price': 11.99, 'image': '06.jpg'},
                    # Adicione mais itens de macarrão conforme necessário
                ],
                # Adicione mais categorias conforme necessário
            }
        }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
