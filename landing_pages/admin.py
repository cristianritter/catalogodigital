from django.contrib import admin
from landing_pages.models import LandingPageData
from import_export.admin import ImportExportModelAdmin

@admin.register(LandingPageData)
class ProductAdmin(ImportExportModelAdmin):
    pass

