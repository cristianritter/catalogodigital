from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cities/florianopolis/catalogodigital/catalogodigital.html')

def ajrcutelaria(request):
    context = {
        'description' : 'Landing page comercio local afiação amolador alicates de unha tesouras facas.',
        'title': 'Adelcio Afiador - Afiação e Venda de Ferramentas para Salões de beleza',
        'static_assets_path': 'cities/sapiranga/ajrcutelaria/assets',
        'sobretitulo_text': 'Afiação e Venda de Ferramentas para Salões de beleza',
        'titulo_text': 'Adélcio Amolador',
        'nossa_historia_content': 'Oferecemos um serviço especializado com mais de 20 anos de experiência. Serviço reconhecido por nossos amigos e clientes.',
        'produtos_servicos_content': 'Serviço especializado de afiação para alicates, tesouras, facas e outras ferramentas profissionais. Temos também uma loja de ferramentas profissionais, incluindo espatulas de cutícula de alta qualidade e uma variedade de acessórios de reposição, de molas metálicas a borrachas de silicone para alicates.',
        'nosso_diferencial_content': 'Oferecemos não apenas serviços e produtos de qualidade, mas também comodidade, pois disponibilizamos atendimento personalizado no seu local de preferência, seja presencial ou remoto. Renove suas ferramentas com praticidade, sem sair do seu espaço de trabalho. Agende uma visita.',
        'promocao_titulo': 'Aproveite nosso desconto exclusivo!',
        'promocao_content': 'Informe que conheceu o nosso local através do nosso site e ganhe 10% de desconto no valor total da sua primeira compra! (Limitado à R$20)',
        'horario_atendimento': 'Seg à Sex das 07-19h.',
        'telefones': '(51) 980159178',
        'endereco': 'Rua Duque de Caxias, 634, Centenário, Sapiranga, RS',
        'whatslink': 'https://wa.me/+5551980159178',
        'gmaps_embed_link': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3468.0310528904797!2d-51.01371158831997!3d-29.631841339516633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95193fbe62929801%3A0xfb885bf48d7148d6!2sAJR%20Cutelaria!5e0!3m2!1sen!2sbr!4v1703100728491!5m2!1sen!2sbr',
    }
    return render(request, 'base_template.html', context)

def residencialvivatorres(request):
    context = {
        'description' : 'Landing page comercio local afiação amolador alicates de unha tesouras facas.',
        'title': 'Alex Amaro - Aluguéis de Verão',
        'static_assets_path': 'cities/sapiranga/ajrcutelaria/assets',
        'sobretitulo_text': 'Afiação e Venda de Ferramentas para Salões de beleza',
        'titulo_text': 'Adélcio Amolador',
        'nossa_historia_content': 'Oferecemos um serviço especializado com mais de 20 anos de experiência. Serviço reconhecido por nossos amigos e clientes.',
        'produtos_servicos_content': 'Serviço especializado de afiação para alicates, tesouras, facas e outras ferramentas profissionais. Temos também uma loja de ferramentas profissionais, incluindo espatulas de cutícula de alta qualidade e uma variedade de acessórios de reposição, de molas metálicas a borrachas de silicone para alicates.',
        'nosso_diferencial_content': 'Oferecemos não apenas serviços e produtos de qualidade, mas também comodidade, pois disponibilizamos atendimento personalizado no seu local de preferência, seja presencial ou remoto. Renove suas ferramentas com praticidade, sem sair do seu espaço de trabalho. Agende uma visita.',
        'promocao_titulo': 'Aproveite nosso desconto exclusivo!',
        'promocao_content': 'Informe que conheceu o nosso local através do nosso site e ganhe 10% de desconto no valor total da sua primeira compra! (Limitado à R$20)',
        'horario_atendimento': 'Seg à Sex das 07-19h.',
        'telefones': '(51) 980159178',
        'endereco': 'Rua Duque de Caxias, 634, Centenário, Sapiranga, RS',
        'whatslink': 'https://wa.me/+5551980159178',
        'gmaps_embed_link': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3468.0310528904797!2d-51.01371158831997!3d-29.631841339516633!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95193fbe62929801%3A0xfb885bf48d7148d6!2sAJR%20Cutelaria!5e0!3m2!1sen!2sbr!4v1703100728491!5m2!1sen!2sbr',
    }
    return render(request, 'base_template.html', context)
