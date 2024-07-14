from django.contrib import admin

from women.models import Women, Categories


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    """
    Admin class for managing Women model in the Django admin interface.
    """
    list_display = ['title', 'is_published', 'time_create', 'get_categories']
    ordering = ['title']
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'time_create']
    filter_horizontal = ('cat',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    list_per_page = 15
    actions = ['set_published', 'set_draft']

    @admin.action(description='Posts are published')
    def set_published(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description='Posts are unpublished')
    def set_draft(self, request, queryset):
        queryset.update(is_published=False)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """
    Admin class for managing Categories in the Django admin interface.
    """
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name',)}
