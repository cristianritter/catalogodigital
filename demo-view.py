import requests
import json

url = 'http://192.168.2.130:8000/set-demo-view/'
dados_json = {
            'static_assets_path': 'cities/florianopolis/catalogodigital/assets',
            'image0link': 'https://img.freepik.com/fotos-gratis/flores-roxas-em-um-vaso_1340-25662.jpg?w=740&t=st=1705512703~exp=1705513303~hmac=0bbdbe0c2b53358feadf03e3fdb58be6fea5ec21c00b928838453ab67cd0530f',
            'image1link': '',
            'image2link': '',
            'image3link': '',            
            'meta_description' : 'Desenvolvimento e hospedagem de landing pages para negócios, marketing e divulgação organica',
            'window_title': 'Catálogo Digital - Seu negócio na Web',
            'sobretitulo': 'Bem Vindo',
            'titulo': 'A melhor landing page para o seu negócio',
            'body_title': 'O que é uma landing page?',
            'body_subtitle': 'Uma landing page é como a vitrine virtual do seu negócio. É uma página da web criada sob medida para você. Imagine-a como a porta de entrada direta para o que sua empresa oferece de melhor. Permita que seus clientes o encontrem com os nossos serviços.',
            'item1_title': 'Presença Online',
            'item1_content': 'Oferecemos um serviço especializado com mais de 20 anos de experiência. Serviço reconhecido por nossos amigos e clientes.',
            'item2_title': 'Credibilidade',
            'item2_content': 'Com um design profissional e informações claras, transmitimos confiança, destacando sua marca de maneira sólida e confiável.',
            'item3_title': 'Publicidade Orgânica',
            'item3_content': 'Ao utilizar nossa plataforma, cada usuário é estimulado a explorar e conhecer outros empreendimentos na mesma área, promovendo uma rede colaborativa que amplia a visibilidade de todos. Assim, seu crescimento não é apenas individual, mas contribui para fortalecer e promover a prosperidade local.',
            'promocao_titulo': 'Aproveite nosso desconto exclusivo de lançamento!',
            'promocao_content': 'Informe que nos encontrou através do nosso site e ganhe 10% de desconto no valor da sua primeira anuidade!',
            'horario_atendimento': 'Seg à Sex das 07-19h.',
            'telefones': '(48) 996810518',
            'whatslink': 'https://wa.me/+5551996810518',
            'email':'cristianritter@gmail.com', 
            'google_share_link': '',
            'endereco': '',
            'gmaps_embed_link': ''}

# Faz uma requisição GET para obter o token CSRF
response_csrf = requests.get(url)
csrftoken = response_csrf.cookies.get('csrftoken', '')

# Faz a requisição POST com o JSON no corpo e o token CSRF no cabeçalho
headers = {'X-CSRFToken': csrftoken, 'Referer': url, 'Content-Type': 'application/json'}
response = requests.post(url, json=dados_json, headers=headers)

# Imprime a resposta do servidor
print("Status Code:", response.status_code)
print("Resposta do servidor:", response.json())
