from django.urls import path

from women import views

app_name = 'women'

urlpatterns = [
    path('', views.index, name='name')
]
