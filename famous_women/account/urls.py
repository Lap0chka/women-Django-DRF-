from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [

    # Login & Logout
    path('login/', views.SingInView.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/posts/', views.profile_posts, name='posts'),
    path('dashboard/update/<slug:slug>', views.UpdatePostView.as_view(), name='update_post'),

    # Register
    path('register/', views.register, name='register'),

]
