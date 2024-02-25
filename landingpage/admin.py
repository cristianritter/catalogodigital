from django.contrib import admin
from landingpage.models import Categoria, LandingPage, Cidade, Empresa, Agendamento, Funcionario, Servico
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin

from django.contrib.auth.models import User, Group

admin.site.site_title = "ConectaPages"
admin.site.site_header = "ConectaPages"
admin.site.index_title = "Gerenciamento do Sistema"

@admin.register(LandingPage)
class LandingPageAdmin(ImportExportModelAdmin):
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            # Se o usuário é um superusuário, ele tem acesso a todos os produtos
            return queryset
        else:
            # Filtra os produtos baseados no usuário logado
            return queryset.filter(owner=request.user)
    
    actions = None
    list_display = ['nome_empresa', 'on_air', 'url', 'numeros_telefone']
    search_fields = ['nome_empresa', 'url']
    list_filter = ('on_air', 'cidades', 'categoria_servico')
    filter_horizontal = ('cidades',)

@admin.register(Cidade)
class CidadesAdmin(ImportExportModelAdmin):
    actions = None
    list_display = ["nome"]
    search_fields = ['nome']


@admin.register(Categoria)
class CategoriaServicoAdmin(ImportExportModelAdmin):
    actions = None
    list_display = ["nome"]
    search_fields = ['nome']

class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    list_display = ('username', 'get_full_name',  'last_login', 'email' )
    search_fields = ('username', 'get_full_name', 'email')
    actions = None

    def get_full_name(self, obj):
        if obj.last_name and obj.first_name:
            return f"{obj.last_name}, {obj.first_name}"
        else:
            return ''
    get_full_name.short_description = 'nome_completo'

class GroupAdmin(ImportExportModelAdmin, BaseGroupAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

@admin.register(Empresa)
class EmpresaAdmin(ImportExportModelAdmin):
    class Meta:
       css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
   
@admin.register(Agendamento)
class AgendamentoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(ImportExportModelAdmin):
    pass

@admin.register(Servico)
class ServicoAdmin(ImportExportModelAdmin):
    pass