from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from women.forms import WomenForm
from women.models import Women, Categories


def index(request):
    """
    Render the 'index.html' template with a context containing all published Women posts.
    """
    posts = Women.published.all().prefetch_related('cat')
    return render(request, 'women/index.html', {
        'posts': posts,
    })


def category_view(request, category):
    """
    Render the 'index.html' template with a context containing all published Women posts belonging to a specific category.
    """
    category = get_object_or_404(Categories, name=category)
    posts = Women.published.filter(cat=category).prefetch_related('cat')
    return render(request, 'women/index.html', {
        'posts': posts,
        'cat_selected': category.pk
    })


def tags_view(request, tags):
    """
    Renders the 'index.html' template to display all published Women posts associated with the provided tags.
    Returns:
        HttpResponse: The HTTP response displaying the Women posts filtered by the provided tags.
    """
    posts = Women.published.filter(tags__name=tags).prefetch_related('cat')
    return render(request, 'women/index.html', {'posts': posts})


def about(request):
    """
       Renders the 'about.html' template to display information about the women's section.
       """
    return render(request, 'women/about.html')


def post(request, post_slug):
    """
Renders the 'post.html' template to display detailed information about a specific woman post identified by the provided slug.
Returns:
    HttpResponse: The HTTP response displaying the detailed information about the specified woman post.
"""
    post = get_object_or_404(Women, slug=post_slug)
    return render(request, 'women/post.html', {'post': post})


def contact(request):
    """
    Renders the contact page for the women's section of the website.
    """
    return render(request, 'women/contact.html')


@login_required
def add_post(request):
    if request.method == 'POST':
        form = WomenForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            category = form.cleaned_data.pop('cat')
            instance.save()
            if category is not None:
                instance.cat.add(category)
            messages.success(request, 'Your post will add.')

    else:
        form = WomenForm()

    return render(request, 'women/add_post.html', {'form': form})
