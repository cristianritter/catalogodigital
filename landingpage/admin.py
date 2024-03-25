from django.contrib import admin
from landingpage.forms import LandingPageForm
from landingpage.models import Category, LandingPage, Cidade, Empresa, Servico
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django_object_actions import DjangoObjectActions 
from landingpage.utils import Storage
from django.contrib.auth.models import User, Group


admin.site.site_title = "ConectaPages"
admin.site.site_header = "ConectaPages"
admin.site.index_title = "Gerenciamento do Sistema"

def clearBucketDirectory(path):
    print('apagando arquivos de: ', path)
    Storage.clear_folder_supabase(path)

class CommonAdmin(DjangoObjectActions, ImportExportModelAdmin):
    # For Actions Buttons and Import/Export Function
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',), # Enables red * on required fields
        }     
    

class FileUploadAdmin(CommonAdmin):
    change_actions = ('clear_bucket_files',)
    readonly_fields = ('image_tag',)

@admin.register(LandingPage)
class LandingPageAdmin(FileUploadAdmin):
    form = LandingPageForm
    actions = None 

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(empresa__owners=request.user)
        
    def clear_bucket_files(self, request, queryset):
        clearBucketDirectory('landingpages/' + str(queryset.id) + '/')  
    readonly_fields = FileUploadAdmin.readonly_fields + ('web_address', 'url',)
    list_display = ['empresa', 'on_air', 'cidadeestado', 'telefones', 'web_address']
    search_fields = ['empresa__name', 'empresa__phone_numbers', 'empresa__address', 'empresa__owners__username']
    list_filter = ['on_air', 'empresa__owners__username']
#    filter_horizontal = ('Cidade',)
  
@admin.register(Cidade)
class CidadesAdmin(ImportExportModelAdmin):
    actions = None
    list_display = ["nome"]
    search_fields = ['nome']

@admin.register(Category)
class CategoriaServicoAdmin(ImportExportModelAdmin):
    actions = None
    list_display = ["name"]
    search_fields = ['name']

@admin.register(Empresa)
class EmpresaAdmin(CommonAdmin):
    class Meta:
       css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
   
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(owners=request.user)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not request.user.is_superuser:
            # Remover os campos que você não quer exibir para usuários não superusuários
            fields = [field for field in fields if field not in ['owners', 'employees']]
        return fields

@admin.register(Servico)
class ServicoAdmin(ImportExportModelAdmin):
    pass

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