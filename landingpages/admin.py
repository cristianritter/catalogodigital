from django.contrib import admin
from landingpages.models import LandingPageData
from import_export.admin import ImportExportModelAdmin

admin.site.site_title = "ConectaPages"
admin.site.site_header = "ConectaPages"
admin.site.index_title = "Gerenciamento do Sistema"

@admin.register(LandingPageData)
class LandingPageDataAdmin(ImportExportModelAdmin):
    actions = None
    list_display = ['nome_empresa', 'on_air', 'url_cadastrado', 'numeros_telefone']
    search_fields = ['nome_empresa', 'url_cadastrado']

