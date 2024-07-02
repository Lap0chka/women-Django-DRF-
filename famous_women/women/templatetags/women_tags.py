from django import template

from women.models import Categories

register = template.Library()


@register.inclusion_tag('women/includes/categories_list.html')
def show_categories(cat_selected=0):
    """
    Render an inclusion tag to display a list of categories.
    """
    cats = Categories.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
