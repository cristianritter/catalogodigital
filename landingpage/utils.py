from django.utils.text import slugify
import os
import supabase
from catalogodigital import settings
from PIL import Image
from io import BytesIO
from django.utils.html import mark_safe



class Generate():
    
    def _generate_whats_number(phone, phone_is_whats):
        if not phone_is_whats: return ""
        clear_number = ''.join(filter(str.isdigit, phone))
        whats_number = "55" + clear_number
        return whats_number

    def _generate_social_links(links):
        dictn = {}
        for link in links:
            if 'facebook' in link:
                dictn['facebook'] = link
            elif 'instagram' in link:
                dictn['instagram'] = link                
        return dictn
    
    def _generate_company_path(company_name, company_address):
         
         return f'{slugify(company_address.split(",")[-1].split("-")[-2]).lower()}/{slugify(company_name)}'

    def _generate_cidade_estado(address):
        return address.split(",")[-1].strip()
    
    def _generate_page_link(company_name, company_address, prefix=''):
        from django.utils.html import mark_safe
        if 'hub' in prefix:
            domain = 'loja.'+settings.DOMAIN
        else:
            domain = settings.DOMAIN
        html_preview = f'<a href="//{domain}/{prefix}{Generate._generate_company_path(company_name, company_address)}" target="_blank">Abrir</a>'
        return mark_safe(html_preview)
    
class Storage():
    
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_SERVICE_ROLE')
    supabase_bucket_name = os.getenv('BUCKET_NAME').upper()
        
    @staticmethod
    def upload_to_supabase(filepath, file_content):
        (filepath, file_content) = Convertions.converter_para_webp(filepath, file_content)
        supabase_client = supabase.create_client(Storage.supabase_url, Storage.supabase_key)
        bucket = supabase_client.storage.get_bucket(Storage.supabase_bucket_name)
        response = bucket.upload( filepath, file_content, 
                                 {'content-type':'image/webp',
                                  'cache-control':'604800'})
        return response
    
    @staticmethod
    def clear_folder_supabase(path):
        print('path',path)
        supabase_client = supabase.create_client(Storage.supabase_url, Storage.supabase_key)
        bucket = supabase_client.storage.get_bucket(Storage.supabase_bucket_name)
        arquivos_list = list(map(lambda d: path+d['name'], bucket.list(os.path.dirname(path))))
        print(arquivos_list)
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

    def converter_para_webp(filepath, file_content):
        img = Image.open(BytesIO(file_content))
        # Converter para o formato WebP
        buffer = BytesIO()
        img.save(buffer, format="WEBP")
        buffer.seek(0)
        filename= ('').join(filepath.split('.')[:-1])+'.webp'
        print(filename)
        return (filename ,buffer.getvalue())
