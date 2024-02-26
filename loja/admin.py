from django.contrib import admin
from loja.models import Hub, Loja, ProductCategory, Item, Cart, CartItem
from import_export.admin import ImportExportModelAdmin

@admin.register(Loja)
class LojaAdmin(ImportExportModelAdmin):
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
    #list_display = ['nome_empresa', 'on_air', 'url']
    #search_fields = ['nome_empresa', 'url']

@admin.register(Hub)
class HubAdmin(ImportExportModelAdmin):
    class Media:
        css = {
            'all': ('common/landing_page/css/admin_styles.css',),
        }
    actions = None
    #list_display = [ 'on_air', 'nome', 'url', 'get_included_lojas']
    #search_fields = ['url', 'nome', 'lojas__url']

    #def get_included_lojas(self, obj):
    #    return ", ".join([loja.url for loja in obj.lojas.all()])
    #get_included_lojas.short_description = 'Lojas Incluídas'

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'store')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'store')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'item', 'quantity')

  