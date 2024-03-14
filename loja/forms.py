from django import forms
from .models import Item, Hub
from landingpage.utils import Storage, Generate
#from django.core.exceptions import ValidationError

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = '__all__'
    #self = None
    
    fileUpload = forms.ImageField(required=False, label='Upload de arquivo')

    def clean_fileUpload(self):        
        numberMaxOfFilesOnDestination = 1
        destinationFolder = Generate._generate_company_path(
                            self.instance.shelf.store.empresa.name, self.instance.shelf.store.empresa.address) + '/store/shelfs/items/'
        
        filesAlreadyOnDestCounter = len(Storage.get_bucket_file_list(destinationFolder))
        if ( filesAlreadyOnDestCounter >= numberMaxOfFilesOnDestination): 
            raise forms.ValidationError(f'O número máximo de arquivos permitidos neste diretório é {numberMaxOfFilesOnDestination}')
        self.save()
            
    def save(self, commit=True):
        instance = super().save(commit=False)
        imageFieldName = 'fileUpload'
        if not self.cleaned_data[imageFieldName]:
            return instance
        
        destinationFolder = Generate._generate_company_path(
                    instance.shelf.store.empresa.name, instance.shelf.store.empresa.address ) + '/store/shelfs/items/'

        try:
            file_content = self.cleaned_data[imageFieldName].read()
            file_name = self.cleaned_data[imageFieldName].name
            Storage.upload_to_supabase(destinationFolder + file_name, file_content)
        except Exception as er:
            print('erro', er)
        if commit:
            instance.save()
        return instance


class HubForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = '__all__'
    
    fileUpload = forms.ImageField(required=False, label='Upload de arquivo')

    def clean_fileUpload(self):        
        numberMaxOfFilesOnDestination = 1
        destinationFolder = Generate._generate_company_path(
                            self.instance.empresa.name, self.instance.empresa.address) + '/'
        
        filesAlreadyOnDestCounter = len(Storage.get_bucket_file_list(destinationFolder))
        if ( filesAlreadyOnDestCounter >= numberMaxOfFilesOnDestination): 
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
            Storage.upload_to_supabase(destinationFolder + file_name, file_content)
        except Exception as er:
            print('erro', er)
        if commit:
            instance.save()
        return instance