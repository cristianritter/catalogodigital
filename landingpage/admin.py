from django.contrib import admin
from landingpage.models import LandingPage, Sistema
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


admin.site.site_title = "ConectaPages"
admin.site.site_header = "ConectaPages"
admin.site.index_title = "Gerenciamento do Sistema"

@admin.register(LandingPage)
class LandingPageAdmin(ImportExportModelAdmin):
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
    list_display = ['nome_empresa', 'on_air', 'url_cadastrado', 'numeros_telefone']
    search_fields = ['nome_empresa', 'url_cadastrado']


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'get_full_name',  'last_login', 'email' )
    search_fields = ('username', 'get_full_name', 'email')
    actions = None

    def get_full_name(self, obj):
        if obj.last_name and obj.first_name:
            return f"{obj.last_name}, {obj.first_name}"
        else:
            return ''
    get_full_name.short_description = 'nome_completo'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Sistema)
class SistemaAdmin(ImportExportModelAdmin):
    actions = None

    list_display = ('on_air', 'config_name', 'repositorio_imagens')