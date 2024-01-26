from django.contrib import admin
from landingpages.models import LandingPageData
from import_export.admin import ImportExportModelAdmin

@admin.register(LandingPageData)
class ProductAdmin(ImportExportModelAdmin):
    pass

