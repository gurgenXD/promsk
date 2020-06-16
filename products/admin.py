from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from products.models import *


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    group_fieldsets = True
    sortable_field_name = 'position'

    fieldsets = (
        (None, {
            'fields': ('parent', 'title', 'column', 'desc'),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
        }),
    )
    list_display = ('title', 'parent', 'column')
    list_editable = ('column',)
    prepopulated_fields = {'slug': ('title',)}


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    classes = ('grp-collapse grp-closed',)


class SimilarProductInline(admin.TabularInline):
    model = SimilarProduct
    fk_name = 'product'
    extra = 0
    classes = ('grp-collapse grp-closed',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'price', 'info', 'desc', 'is_active'),
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'info', 'desc', )
    list_display = ('title', 'category', 'price', 'is_active')
    list_editable = ('is_active',)

    inlines = (ImageInline, SimilarProductInline)

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )