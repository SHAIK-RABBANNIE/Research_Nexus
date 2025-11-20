from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def projects_view(request):
    return render(request, 'projects.html')

def repositories_view(request):
    return render(request, 'repositories.html')

def collaborators_view(request):
    return render(request, 'collaborators.html')

def analytics_view(request):
    return render(request, 'analytics.html')

def settings_view(request):
    return render(request, 'settings.html')

def logout_view(request):
    # Clear any session data
    request.session.flush()
    # Redirect to login page
    return redirect('login')