import requests

url = 'http://192.168.2.130:8000/set_demo_view/'
#url = 'https://catalogodigital-437b69889213.herokuapp.com/set_demo_view/'
dados_json = {
            'static_assets_path': 'cities/florianopolis/catalogodigital/assets',
            'image0link': 'https://img.freepik.com/fotos-gratis/arranjo-lindo-de-papel-de-parede-de-flores_23-2149057015.jpg?w=740&t=st=1705514234~exp=1705514834~hmac=1713136e4e62e730ee095c34beb70f15c0bf164e0e2beaedf0dec25cbd6ec2eb',
            'image1link': 'https://img.freepik.com/fotos-gratis/flores-roxas-com-uma-bela-vista-da-ilha-da-madeira-em-portugal_181624-27202.jpg?size=626&ext=jpg&ga=GA1.1.177824122.1705512621&semt=sph',
            'image2link': 'https://img.freepik.com/fotos-gratis/flores-cor-de-rosa-em-rosa_24837-301.jpg?w=740&t=st=1705513525~exp=1705514125~hmac=a6a67ae86580b495f7b5208352f669f2c0412795cc54687c9ecb2bbe77cec712',
            'image3link': 'https://img.freepik.com/fotos-premium/as-flores-no-jardim-estao-florescendo-em-uma-bela-primavera_215913-135.jpg?w=740',            
            'meta_description' : 'Desenvolvimento e hospedagem de landing pages para negócios, marketing e divulgação organica',
            'window_title': 'Catálogo Digital - Seu negócio na Web',
            'sobretitulo': 'Seja Bem Vindo',
            'titulo': 'Floricultura Central',
            'body_title': 'Seja bem vindo',
            'body_subtitle': 'Nossa floricultura presta serviços especializados desde 2023.',
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
            'google_share_link': 'https://maps.app.goo.gl/pTZvag2fg7ytV74eA',
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
