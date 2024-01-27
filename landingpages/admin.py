from django.contrib import admin
from landingpages.models import LandingPageData
from import_export.admin import ImportExportModelAdmin

@admin.register(LandingPageData)
class LandingPageDataAdmin(ImportExportModelAdmin):
    pass
    list_display = ['nome_empresa', 'url_cadastrado', 'numeros_telefone']
    search_fields = ['nome_empresa', 'url_cadastrado']

