from django.urls import path, include

from api import views

urlpatterns = [
    path('womenlist/', views.WomenApiView.as_view(), name='api_list'),
    path('women/update/<int:pk>', views.WomenApiUpdate.as_view(), name='api_update'),
    path('women/deteil/<int:pk>', views.WomenApiDetail.as_view(), name='api_deteil')
]
