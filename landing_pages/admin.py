from django.contrib import admin
from landing_pages.models import LandingPageData, ModelRoute, ModelView
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(LandingPageData)
class ProductAdmin(ImportExportModelAdmin):
    pass


admin.site.register(ModelRoute)
admin.site.register(ModelView)