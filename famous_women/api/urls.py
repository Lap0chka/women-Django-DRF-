from django.urls import path, include

from api import views

urlpatterns = [
    path('v1/womenlist', views.WomenApiView.as_view(), name='api_list')
]
