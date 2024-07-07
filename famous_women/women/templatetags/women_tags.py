from django import template

from women.models import Categories, Women

register = template.Library()


@register.inclusion_tag('women/templates_tags/categories_list.html')
def show_categories(cat_selected=0):
    """
    Render an inclusion tag to display a list of categories.
    """
    cats = Categories.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/templates_tags/tags_list.html')
def show_tags():
    """
    Return a dictionary containing the 'tags' key with the value of the 'tags' variable.
    """
    tags = Women.tags.all()
    return {'tags': tags}
