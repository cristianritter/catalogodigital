from django.contrib import admin
from loja.models import Hub, Store, Shelf, Item
from import_export.admin import ImportExportModelAdmin
from .forms import ItemForm, HubForm, StoreForm
from landingpage.admin import CommonAdmin
from landingpage.utils import Storage

def clearBucketDirectory(path):
    print('apagando arquivos de: ', path)
    Storage.clear_folder_supabase(path)

class FileUploadAdmin(CommonAdmin):
    change_actions = ('clear_bucket_files',)
    readonly_fields = ('image_tag',)

@admin.register(Store)
class StoreAdmin(FileUploadAdmin):
    form = StoreForm
    readonly_fields = FileUploadAdmin.readonly_fields + ('web_address', 'url',)
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
    def clear_bucket_files(self, request, queryset):
        clearBucketDirectory('stores/' + str(queryset.id) + '/')

    #readonly_fields = ('image_filename',)
    #list_display = ['nome_empresa', 'on_air', 'url']
    #search_fields = ['nome_empresa', 'url']

@admin.register(Hub)
class HubAdmin(FileUploadAdmin):
    form = HubForm
    readonly_fields = FileUploadAdmin.readonly_fields + ('web_address', 'url',)
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
    def clear_bucket_files(self, request, queryset):
        clearBucketDirectory('hubs/' + str(queryset.id) + '/')

    #list_display = [ 'on_air', 'nome', 'url', 'get_included_lojas']
    #search_fields = ['url', 'nome', 'lojas__url']


@admin.register(Shelf)
class ShelfAdmin(ImportExportModelAdmin):
    list_display = ('name', 'store')

@admin.register(Item)
class ItemAdmin(FileUploadAdmin):
    form = ItemForm
    readonly_fields = FileUploadAdmin.readonly_fields + ('image_filename',)
    list_display = ('name', 'price', 'description')
    def clear_bucket_files(self, request, queryset):
       clearBucketDirectory('items/' + str(queryset.id) + '/')




  