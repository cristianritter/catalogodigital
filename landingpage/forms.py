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

    uploadType = forms.ChoiceField(choices=[('cover', 'Imagem de Capa'), ('carousel', 'Imagem de Carrosel')], label='O que você está enviando?')
    fileUploadField = forms.ImageField(required=False, label='Upload de arquivo')

    def clean_fileUpload(self):    
        numberMaxOfFilesOnDestination = 6
        
        filesAlreadyOnDestCounter = len(Storage.get_bucket_file_list(self.destFolder))
        print(filesAlreadyOnDestCounter)
        if ( filesAlreadyOnDestCounter >= numberMaxOfFilesOnDestination and self.cleaned_data[self.fileUploadField]): 
            raise forms.ValidationError(f'O número máximo de arquivos permitidos neste diretório é {numberMaxOfFilesOnDestination}')
        self.save()
            
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
