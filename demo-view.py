import requests

url = 'https://www.mk4digital.com/set_demo_view/'
dados_json = {
            'img0': 'https://img.freepik.com/fotos-gratis/arranjo-lindo-de-papel-de-parede-de-flores_23-2149057015.jpg?w=740&t=st=1705514234~exp=1705514834~hmac=1713136e4e62e730ee095c34beb70f15c0bf164e0e2beaedf0dec25cbd6ec2eb',
            'img1': 'https://img.freepik.com/fotos-gratis/flores-roxas-com-uma-bela-vista-da-ilha-da-madeira-em-portugal_181624-27202.jpg?size=626&ext=jpg&ga=GA1.1.177824122.1705512621&semt=sph',
            'img2': 'https://img.freepik.com/fotos-gratis/flores-cor-de-rosa-em-rosa_24837-301.jpg?w=740&t=st=1705513525~exp=1705514125~hmac=a6a67ae86580b495f7b5208352f669f2c0412795cc54687c9ecb2bbe77cec712',
            'img3': 'https://img.freepik.com/fotos-premium/as-flores-no-jardim-estao-florescendo-em-uma-bela-primavera_215913-135.jpg?w=740',            
            'static_assets_path': 'cities/torres/residencialvivatorres/assets',
            'carousel_counter': range(3),
            'meta_description' : 'Landing page comercio local afiação amolador alicates de unha tesouras facas em Sapiranga Rio Grande do Sul.',
            'window_title': 'Adelcio Afiador - Afiação e Venda de Ferramentas para Salões de beleza',
            'sobretitulo': 'Afiação e Venda de Ferramentas para Salões de beleza',
            'titulo': 'Adélcio Amolador',
            'body_title': 'Produtos e Serviços',
            'lista_servicos': ['Afiação de Alicates e Tesouras', 'Afiação de facas', 'Venda de Ferramentas', 'Atendimento à domicílio', 'Consulte as regiões de cobertura'],
            'item1_title': 'Nossa História',
            'item1_content': 'Oferecemos um serviço especializado com mais de 20 anos de experiência. Serviço reconhecido por nossos amigos e clientes.',
            'item2_title': 'Tudo o que você precisa',
            'item2_content': 'Serviço especializado de afiação para alicates, tesouras, facas e outras ferramentas profissionais. Temos também uma loja de ferramentas profissionais, incluindo espatulas de cutícula de alta qualidade e uma variedade de acessórios de reposição, de molas metálicas a borrachas de silicone para alicates.',
            'item3_title': 'Nosso Diferencial',
            'item3_content': 'Oferecemos não apenas serviços e produtos de qualidade, mas também comodidade, pois disponibilizamos atendimento personalizado no seu local de preferência, seja presencial ou remoto. Renove suas ferramentas com praticidade, sem sair do seu espaço de trabalho. Agende uma visita.',
            'promocao_content': 'Informe que conheceu a empresa através do site e ganhe 10% de desconto no valor total da sua primeira compra! (Limitado à R$10)',
            'horario_atendimento': 'Seg à Sex das 07-19h.',
            'telefones': '(51) 980159178',
            'email':'', 
            'whatslink': 'https://wa.me/+5551980159178',
            'google_share_link': 'https://maps.app.goo.gl/pTZvag2fg7ytV74eA',
            'endereco': 'Rua Duque de Caxias, 634, Centenário, Sapiranga, RS',
            'gmaps_embed_link': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3468.0310528904797!2d-51.01371158831997!3d-29.631841339516633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95193fbe62929801%3A0xfb885bf48d7148d6!2sAJR%20Cutelaria!5e0!3m2!1sen!2sbr!4v1703100728491!5m2!1sen!2sbr',
}

dados_json['img_links'] = [dados_json['img0'], dados_json['img1'], dados_json['img2'], dados_json['img3']]

# Faz uma requisição GET para obter o token CSRF
response_csrf = requests.get(url)
csrftoken = response_csrf.cookies.get('csrftoken', '')

# Faz a requisição POST com o JSON no corpo e o token CSRF no cabeçalho
headers = {'X-CSRFToken': csrftoken, 'Referer': url, 'Content-Type': 'application/json'}
response = requests.post(url, json=dados_json, headers=headers)

# Imprime a resposta do servidor
print("Status Code:", response.status_code)
print("Resposta do servidor:", response.json())
