from django.contrib import admin
from lojas.models import Loja
from import_export.admin import ImportExportModelAdmin

@admin.register(Loja)
class LojaAdmin(ImportExportModelAdmin):
    pass
