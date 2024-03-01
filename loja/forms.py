from django import forms
from .models import Item
import supabase
import os


def upload_to_supabase(bucket_name, file_content):
    # Configuração do cliente Supabase
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_ANON_KEY')
    supabase_client = supabase.create_client(supabase_url, supabase_key)
    bucket = supabase_client.storage._create_session()
    print(bucket)
    response = bucket.upload(file_content, f"images/")

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    imagem = forms.ImageField(required=False)

    #def save(self, commit=True):
    #    instance = super().save(commit=False)
        #file_content = self.cleaned_data['imagem'].read()
        #instance.imagem_url = upload_to_supabase('teste', file_content)
        #if commit:
        #    instance.save()
        #return instance
