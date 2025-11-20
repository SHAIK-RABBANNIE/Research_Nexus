from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('projects/', views.projects_view, name='projects'),
    path('repositories/', views.repositories_view, name='repositories'),
    path('collaborators/', views.collaborators_view, name='collaborators'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('settings/', views.settings_view, name='settings'),
    path('logout/', views.logout_view, name='logout'),  # Add this line
]