from django.shortcuts import render, get_object_or_404

from women.models import Women


def index(reqeust):
    posts = Women.published.all()
    return render(reqeust, 'women/index.html', {'posts':posts})


def about(reqeust):
    return render(reqeust, 'women/about.html')


def post(reqeust, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    return render(reqeust, 'women/post.html', {'post': post})


def contact(reqeust):
    return render(reqeust, 'women/contact.html')
