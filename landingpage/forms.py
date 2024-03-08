from django import forms
from .models import LandingPage
from landingpage.utils import Storage, Generate
from django.core.exceptions import ValidationError

class LandingPageForm(forms.ModelForm):
    
    class Meta:
        model = LandingPage
        fields = '__all__'

    fileUpload = forms.ImageField(required=False, label='Upload de arquivo')
    
    def clean_fileUpload(self):
        if not self.cleaned_data['fileUpload']:
            return
        upload_file_name = self.cleaned_data['fileUpload'].name.lower()
        if (
            len(
                Storage.get_bucket_file_list(
                    Generate._generate_company_path(
                        self.instance.empresa.name, self.instance.empresa.address
                    )+'/'
                )
            )
        >= 6): 
            raise forms.ValidationError('O número máximo de imagens para uma landing page é 6')
        elif (len(upload_file_name) != 6 or not '.webp' in upload_file_name ):
            raise forms.ValidationError('O nome ou a extensão do arquivo está incorreta.')
        self.save()
            

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not self.cleaned_data['fileUpload']:
            return instance
        try:
            file_content = self.cleaned_data['fileUpload'].read()
            file_name = self.cleaned_data['fileUpload'].name
            company_path = Generate._generate_company_path(
                    instance.empresa.name,
                    instance.empresa.address )
            Storage.upload_to_supabase(company_path+ '/' + file_name, file_content )
        except Exception as er:
            print('erro', er)
        if commit:
            instance.save()
        return instance
