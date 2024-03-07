from django.utils.text import slugify
import os
import supabase

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
    
    def _generate_url(company_name, company_address):
         return f'{slugify(company_address).split("-")[-2].lower()}/{slugify(company_name)}'
    
class Storage():
    
    def upload_to_supabase(bucket_name, filepath, file_content):
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_SERVICE_ROLE')
        supabase_client = supabase.create_client(supabase_url, supabase_key,)
        bucket = supabase_client.storage.get_bucket(bucket_name)
        response = bucket.upload( filepath, file_content, 
                                 {'content-type':'image/webp',
                                  'cache-control':'604800'})
        return response
    
    def clear_folder_supabase(bucket_name, path):
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_SERVICE_ROLE')
        supabase_client = supabase.create_client(supabase_url, supabase_key,)
        bucket = supabase_client.storage.get_bucket(bucket_name)
        arquivos_list = list(map(lambda d: d['name'], bucket.list(os.path.dirname(path))))
        response = bucket.remove(arquivos_list)
        return response
    
    def get_bucket_url(bucket_name):
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_SERVICE_ROLE')
        supabase_client = supabase.create_client(supabase_url, supabase_key,)
        bucket = supabase_client.storage.get_bucket(bucket_name)
        url = bucket.get_public_url('')[:-1]
        return url
    
    def get_bucket_file_list(bucket_name, path):
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_SERVICE_ROLE')
        supabase_client = supabase.create_client(supabase_url, supabase_key,)
        bucket = supabase_client.storage.get_bucket(bucket_name)
        arquivos_list = list(map(lambda d: d['name'], bucket.list(os.path.dirname(path))))
        return arquivos_list
