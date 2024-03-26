from django.utils.text import slugify
import os
import supabase
from catalogodigital import settings
from PIL import Image
from io import BytesIO
from django.utils.html import mark_safe

class Generate():
    
    def _generate_whats_number(phone):
        clear_number = ''.join(filter(str.isdigit, phone))
        whats_number = "55" + clear_number
        print(whats_number)
        return whats_number

    def _generate_social_links(links : str):
        dictn = {}
        for link in links.splitlines():
            if 'facebook' in link:
                dictn['facebook'] = link
            elif 'instagram' in link:
                dictn['instagram'] = link    
        return dictn
    
    def _generate_company_path(company_name, company_address):
         
         return f'{slugify(company_address.split(",")[-1].split("-")[-2]).lower()}/{slugify(company_name)}'

    def _generate_cidade_estado(address):
        return address.split(",")[-1].strip()
    
    def _generate_web_address(company_name, company_address, prefix=''):
        from django.utils.html import mark_safe
        if 'hub' in prefix:
            domain = 'loja.'+settings.DOMAIN
        else:
            domain = settings.DOMAIN
        html_preview = f'<a href="//{domain}/{prefix}{Generate._generate_company_path(company_name, company_address)}" target="_blank">Visualizar</a>'
        return mark_safe(html_preview)
    
class Storage():
    
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_SERVICE_ROLE')
    supabase_bucket_name = os.getenv('BUCKET_NAME').upper()
        
    @staticmethod
    def upload_to_supabase(filepath, file_content, size: tuple, quality=90):
        file_content = Convertions.convertImageToWebp(file_content, size, quality=quality)
        supabase_client = supabase.create_client(Storage.supabase_url, Storage.supabase_key)
        bucket = supabase_client.storage.get_bucket(Storage.supabase_bucket_name)
        response = bucket.upload( filepath, file_content, 
                                 {'content-type':'image/webp',
                                  'cache-control':'7200'})
        return response
    
    @staticmethod
    def clear_folder_supabase(path):
        print('path',path)
        supabase_client = supabase.create_client(Storage.supabase_url, Storage.supabase_key)
        bucket = supabase_client.storage.get_bucket(Storage.supabase_bucket_name)
        arquivos_list = list(map(lambda d: path+d['name'], bucket.list(os.path.dirname(path))))
        print(arquivos_list)
        response = "Diretório vazio."
        if (len(arquivos_list) > 0):
            response = bucket.remove(arquivos_list)
        return response
    
    @staticmethod
    def get_bucket_url(path):
        supabase_client = supabase.create_client(Storage.supabase_url, Storage.supabase_key)
        bucket = supabase_client.storage.get_bucket(Storage.supabase_bucket_name)
        url = bucket.get_public_url(path).replace('?','')
        return url
    
    @staticmethod
    def get_bucket_file_list(path):
        supabase_client = supabase.create_client(Storage.supabase_url, Storage.supabase_key)
        bucket = supabase_client.storage.get_bucket(Storage.supabase_bucket_name)
        dir = os.path.dirname(path)
        arquivos_list = list(map(lambda d: d['name'], bucket.list(dir))) # somedir/somefile
        return arquivos_list
 
    @staticmethod    
    def get_image_tag(path=''):
        print(path)
        html_preview = ""
        bucket_link = Storage.get_bucket_url(path+'/')
        for file in Storage.get_bucket_file_list(path+'/'):
            print('files in bucket: ', file)
            if not '.webp' in file:
                print('continuou')
                continue
            # Adiciona a tag HTML para a imagem com o nome do arquivo ao lado
            html_preview += f'<div style="display: flex; align-items: center;">'
            html_preview += f'<img src="{bucket_link}/{file}" width="120" height="auto" />'
            html_preview += f'<a href="{bucket_link}/{file}" target="_blank" style="margin-left: 10px;">{file}</a></div>'
        return mark_safe(html_preview)
    
class Convertions():

 def convertImageToWebp(file_content, size, quality=100):
    img = Image.open(BytesIO(file_content))

    # Redimensionar para que a altura ou largura seja igual ao valor máximo especificado
    largura, altura = size
    largura_original, altura_original = img.size
    proporcao = max(largura / largura_original, altura / altura_original)
    nova_largura = int(largura_original * proporcao)
    nova_altura = int(altura_original * proporcao)
    img = img.resize((nova_largura, nova_altura))

    # Fazer corte (crop)
    esquerda = (nova_largura - largura) // 2
    topo = (nova_altura - altura) // 2
    direita = esquerda + largura
    inferior = topo + altura
    img = img.crop((esquerda, topo, direita, inferior))

    # Converter para o formato WebP
    buffer = BytesIO()
    img.save(buffer, format="WEBP", quality=quality, optimize=True)
    buffer.seek(0)
    return (buffer.getvalue())