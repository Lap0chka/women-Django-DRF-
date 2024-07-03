from django.shortcuts import render, get_object_or_404

from women.models import Women, Categories


def index(reqeust):
    """
    Render the 'index.html' template with a context containing all published Women posts.
    """
    posts = Women.published.all()

    return render(reqeust, 'women/index.html', {
        'posts': posts,
    })


def category_view(reqeust, category):
    """
    Render the 'index.html' template with a context containing all published Women posts belonging to a specific category.
    """
    category = get_object_or_404(Categories, name=category)
    posts = Women.published.filter(cat=category)
    return render(reqeust, 'women/index.html', {
        'posts': posts,
        'cat_selected': category.pk
    })


def about(reqeust):
    return render(reqeust, 'women/about.html')


def post(reqeust, post_slug):
    """
    Renders the 'about.html' template to display information about the women's section.
    """
    post = get_object_or_404(Women, slug=post_slug)
    return render(reqeust, 'women/post.html', {'post': post})


def contact(reqeust):
    """
    Renders the contact page for the women's section of the website.
    """
    return render(reqeust, 'women/contact.html')
