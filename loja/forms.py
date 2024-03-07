from django import forms
from .models import Item
from landingpage.utils import Storage

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    imagem = forms.ImageField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        try:
            file_content = self.cleaned_data['imagem'].read()
            instance.imagem_url = Storage.upload_to_supabase('teste', file_content)
        except Exception as er:
            print('erro', er)
            pass
        if commit:
            instance.save()
        return instance
