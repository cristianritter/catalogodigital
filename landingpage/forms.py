from django import forms
from .models import LandingPage
from landingpage.utils import Storage
from catalogodigital import settings

class LandingPageForm(forms.ModelForm):
    class Meta:
        model = LandingPage
        fields = '__all__'

    FileUpload = forms.ImageField(required=False, label='Upload de arquivo')
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        try:
            file_content = self.cleaned_data['FileUpload'].read()
            file_name = self.cleaned_data['FileUpload'].name
            Storage.upload_to_supabase(settings.BUCKET_NAME, file_name, file_content)
        except Exception as er:
            print('erro', er)
            pass
        if commit:
            instance.save()
        return instance
