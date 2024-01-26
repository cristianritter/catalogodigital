from django.contrib import admin
from lojas.models import LojaData
from import_export.admin import ImportExportModelAdmin

@admin.register(LojaData)
class ProductAdmin(ImportExportModelAdmin):
    pass