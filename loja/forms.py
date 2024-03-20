from django import forms
from .models import Item, Hub, Store
from landingpage.utils import Storage

def cleanImageCounter(self):
    if (self.cleaned_data[self.fileUploadField] != None):
            filesAlreadyOnDestCounter = len(Storage.get_bucket_file_list(self.destFolder))
            print('files:', filesAlreadyOnDestCounter)
            if ( filesAlreadyOnDestCounter >= self.numberMaxOfFilesOnDestination): 
                raise forms.ValidationError(f'O número máximo de arquivos permitidos neste diretório é {self.numberMaxOfFilesOnDestination}')
    self.save()
    

class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.destFolder = 'items/' + str(self.instance.id) + '/'   
            self.fileUploadField = 'fileUploadField'
            self.numberMaxOfFilesOnDestination = 1
        except Exception as err: print(err)
    class Meta:
        model = Item
        fields = '__all__'
    
    fileUploadField = forms.ImageField(required=False, label='Upload de arquivo')
 
    def clean_fileUploadField(self):         
        cleanImageCounter(self)
            
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not self.cleaned_data[self.fileUploadField]:
            print('retornou')
            return instance
        print('instancia',instance)
 
        try:
            file_content = self.cleaned_data[self.fileUploadField].read()
            file_name = self.cleaned_data[self.fileUploadField].name
            Storage.upload_to_supabase(self.destFolder + '/' + file_name, file_content, (250,250))
        except Exception as er:
            print('erro', er)
        if commit:
            instance.save()
        return instance


class StoreForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.destFolder = 'stores/' + str(self.instance.id) + '/'  
            self.fileUploadField = 'fileUploadField'
            self.numberMaxOfFilesOnDestination = 1
        except: pass
    class Meta:
        model = Store
        fields = '__all__'

    uploadType = forms.ChoiceField(choices=[('cover', 'Imagem de capa'), ('logo', 'Imagem de Logotipo')], label='O que você está enviando?')
    fileUploadField = forms.ImageField(required=False, label='Upload de arquivo')

    def clean_fileUploadField(self):        
        cleanImageCounter(self)
            
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not self.cleaned_data[self.fileUploadField]:
            return instance
        
        try:
            file_content = self.cleaned_data[self.fileUploadField].read()
            file_name = self.cleaned_data[self.fileUploadField].name
            if self.cleaned_data['uploadType'] == 'cover':
                size = (800,400)
            if self.cleaned_data['uploadType'] == 'logo':
                size = (150, 150)
            Storage.upload_to_supabase(self.destFolder + '/' + file_name, file_content, size)
        except Exception as er:
            print('erro', er)
        
        if commit:
            instance.save()
        return instance

class HubForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.destFolder = 'hubs/' + str(self.instance.id) + '/'  
            self.fileUploadField = 'fileUploadField'
            self.numberMaxOfFilesOnDestination = 1
        except: pass
    class Meta:
        model = Hub
        fields = '__all__'
    
    fileUploadField = forms.ImageField(required=False, label='Upload de arquivo')


    def clean_fileUploadField(self):        
        cleanImageCounter(self)
            
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not self.cleaned_data[self.fileUploadField]:
            return instance
        
        try:
            file_content = self.cleaned_data[self.fileUploadField].read()
            file_name = self.cleaned_data[self.fileUploadField].name
            Storage.upload_to_supabase(self.destFolder + '/' + file_name, file_content, size=(800,400))
        except Exception as er:
            print('erro', er)
        
        if commit:
            instance.save()
        return instance