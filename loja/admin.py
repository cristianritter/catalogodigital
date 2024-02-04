from django.contrib import admin
from loja.models import Loja
from import_export.admin import ImportExportModelAdmin

@admin.register(Loja)
class LojaAdmin(ImportExportModelAdmin):
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
    list_display = ['nome_empresa', 'on_air', 'url_cadastrado']
    search_fields = ['nome_empresa', 'url_cadastrado']

  