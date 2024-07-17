from django.urls import path

from women import views

app_name = 'women'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category>', views.category_view, name='index_cat'),
    path('tags/<str:tags>', views.tags_view, name='index_tag'),
    path('article/<slug:post_slug>', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add_post/', views.add_post, name='add_post')
]
