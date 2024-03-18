from django import forms
from .models import LandingPage
from landingpage.utils import Storage, Generate
#from django.core.exceptions import ValidationError

class LandingPageForm(forms.ModelForm):
    
    class Meta:
        model = LandingPage
        fields = '__all__'
    
    fileUpload = forms.ImageField(required=False, label='Upload de arquivo')

    def clean_fileUpload(self):    
        imageFieldName = 'fileUpload'    
        numberMaxOfFilesOnDestination = 6
        destinationFolder = Generate._generate_company_path(
                            self.instance.empresa.name, self.instance.empresa.address) + '/'
        
        filesAlreadyOnDestCounter = len(Storage.get_bucket_file_list(destinationFolder))
        print(filesAlreadyOnDestCounter)
        if ( filesAlreadyOnDestCounter >= numberMaxOfFilesOnDestination and self.cleaned_data[imageFieldName]): 
            raise forms.ValidationError(f'O número máximo de arquivos permitidos neste diretório é {numberMaxOfFilesOnDestination}')
        self.save()
            
    def save(self, commit=True):
        instance = super().save(commit=False)
        imageFieldName = 'fileUpload'
        if not self.cleaned_data[imageFieldName]:
            return instance
        
        destinationFolder = Generate._generate_company_path(
                    instance.empresa.name, instance.empresa.address ) + '/'

        try:
            file_content = self.cleaned_data[imageFieldName].read()
            file_name = self.cleaned_data[imageFieldName].name
            Storage.upload_to_supabase(destinationFolder+ file_name, file_content)
        except Exception as er:
            print('erro', er)
        if commit:
            instance.save()
        return instance
