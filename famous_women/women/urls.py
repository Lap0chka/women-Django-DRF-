from django.urls import path

from women import views

app_name = 'women'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<slug:post_slug>', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
