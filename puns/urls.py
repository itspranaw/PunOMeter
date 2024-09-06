from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.puns_list, name='puns_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='puns/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='puns/logout.html'), name='logout'),
    path('submit/', views.submit_pun, name='submit_pun'),
    path('rate/<int:pun_id>/', views.rate_pun, name='rate_pun'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
