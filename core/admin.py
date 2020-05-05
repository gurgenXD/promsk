from django.contrib import admin
from core.models import *


admin.site.register(MailFromString)
admin.site.register(MailToString)
admin.site.register(TitleTag)


class ProductInIndexInline(admin.TabularInline):
    model = ProductInIndex
    extra = 0
    classes = ('grp-collapse grp-closed',)


class CategoryInIndexInline(admin.TabularInline):
    model = CategoryInIndex
    extra = 0
    classes = ('grp-collapse grp-closed',)


class ProcInline(admin.TabularInline):
    model = Proc
    extra = 0
    classes = ('grp-collapse grp-closed',)


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    # class Media:
    #     js = (
    #         '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
    #         '/static/grappelli/tinymce_setup/tinymce_setup.js',
    #     )

    inlines = (CategoryInIndexInline, ProductInIndexInline, ProcInline)