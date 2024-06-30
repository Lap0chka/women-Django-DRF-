from django.shortcuts import render, get_object_or_404

from women.models import Women, Categories


def index(reqeust, category=None):
    posts = Women.published.all()
    if category:
        posts = Women.objects.filter(is_published=True, categories__name=category)
    cats = Categories.objects.all()
    return render(reqeust, 'base.html', {
        'posts': posts,
        'cats': cats,
    })


def about(reqeust):
    return render(reqeust, 'women/about.html')


def post(reqeust, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    return render(reqeust, 'women/post.html', {'post': post})


def contact(reqeust):
    return render(reqeust, 'women/contact.html')
