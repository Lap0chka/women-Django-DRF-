from django.contrib import admin

from women.models import Women, Categories


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    """
    Admin class for managing Women model in the Django admin interface.
    """
    list_display = ['title', 'is_published', 'get_categories']
    filter_horizontal = ('cat',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """
    Admin class for managing Categories in the Django admin interface.
    """
    list_display = ['name', ]

    prepopulated_fields = {'slug': ('name',)}
