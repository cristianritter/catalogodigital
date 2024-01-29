from django.contrib import admin
from landingpages.models import LandingPage
from import_export.admin import ImportExportModelAdmin

admin.site.site_title = "ConectaPages"
admin.site.site_header = "ConectaPages"
admin.site.index_title = "Gerenciamento do Sistema"

@admin.register(LandingPage)
class LandingPageAdmin(ImportExportModelAdmin):
    actions = None
    list_display = ['nome_empresa', 'on_air', 'url_cadastrado', 'numeros_telefone']
    search_fields = ['nome_empresa', 'url_cadastrado']

