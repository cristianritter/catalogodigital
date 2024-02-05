from django.contrib import admin
from loja.models import Hub, Loja
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

@admin.register(Hub)
class HubAdmin(ImportExportModelAdmin):
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
    list_display = [ 'on_air', 'url', 'get_included_lojas']
    search_fields = ['url', 'get_included_lojas']

    def get_included_lojas(self, obj):
        return ", ".join([loja.url_cadastrado for loja in obj.lojas.all()])
    get_included_lojas.short_description = 'Lojas Incluídas'


  