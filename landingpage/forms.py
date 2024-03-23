from django import forms
from .models import LandingPage
from landingpage.utils import Storage
#from django.core.exceptions import ValidationError

class LandingPageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.destFolder = 'landingpages/' + str(self.instance.id) + '/'  
            self.fileUploadField = 'fileUploadField'
            self.numberMaxOfFilesOnDestination = 1
        except: pass
    class Meta:
        model = LandingPage
        fields = '__all__'

    uploadType = forms.ChoiceField(choices=[('nothing', 'Nenhum arquivo'), ('cover', 'Imagem de Capa'), ('carousel', 'Imagem de Carrosel')], label='O que você está enviando?', 
                                   help_text="Imagens de carrousel devem ser enviadas em sequencia, numeradas no nome do arquivo a partir de 2")
    fileUploadField = forms.ImageField(required=False, label='Upload de arquivo')

    def clean(self):
        cleaned_data = super().clean()
        upload_type = cleaned_data.get('uploadType')
        file_upload = cleaned_data.get('fileUploadField')
        number_max_of_files = 6
        
        if upload_type == 'nothing' and file_upload:
            raise forms.ValidationError('Selecione o tipo de imagem que está enviando.')

        files_already_on_dest_counter = len(Storage.get_bucket_file_list(self.destFolder))
        if files_already_on_dest_counter >= number_max_of_files and file_upload:
            raise forms.ValidationError(f'O número máximo de arquivos permitidos neste diretório é {number_max_of_files}')

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not self.cleaned_data[self.fileUploadField]:
            return instance
        try:
            file_content = self.cleaned_data[self.fileUploadField].read()
            file_name = self.cleaned_data[self.fileUploadField].name
            if self.cleaned_data['uploadType'] == 'cover':
                size = (400,400)
                Storage.upload_to_supabase(self.destFolder + 'heading_large.webp', file_content, size, quality=100)
                Storage.upload_to_supabase(self.destFolder + 'heading_small.webp', file_content, size, quality=20)
            if self.cleaned_data['uploadType'] == 'carousel':
                size = (350, 200)
                Storage.upload_to_supabase(self.destFolder + file_name.split('.')[0] +'.webp', file_content, size, quality=100)

        except Exception as er:
            print('erro', er)
        if commit:
            instance.save()
        return instance
