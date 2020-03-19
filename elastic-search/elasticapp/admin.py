from django.contrib import admin
from .models import Post, Banks, Branches
# Register your models here.
from import_export.admin import ImportExportModelAdmin


from import_export.admin import ImportExportActionModelAdmin

# class BookAdmin(ImportExportActionModelAdmin):
#     pass
#
from import_export import resources

class BookResource(resources.ModelResource):

    class Meta:
        model = Banks


class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource


admin.site.register(Post)

admin.site.register(Banks, BookAdmin)

admin.site.register(Branches)