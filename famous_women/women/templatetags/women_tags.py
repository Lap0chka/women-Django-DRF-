from django import template

from women.models import Categories

register = template.Library()


@register.inclusion_tag('women/includes/categories_list.html')
def show_categories(cat_selected=0):
    cats = Categories.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
