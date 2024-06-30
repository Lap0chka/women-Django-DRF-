from django.contrib import admin

from women.models import Women, Categories


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'get_categories']
    filter_horizontal = ('categories',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', ]

    prepopulated_fields = {'slug': ('name',)}
