from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

def home_view(request):
    endpoints = [
        {"name": "Inscription", "url": "https://teddsk.pythonanywhere.com/signup/", "method": "POST"},
        {"name": "Connexion", "url": "https://teddsk.pythonanywhere.com/login/", "method": "POST"},
        {"name": "Déconnexion", "url": "https://teddsk.pythonanywhere.com/logout/", "method": "GET"},
    ]
    return render(request, "auth/home.html", {"endpoints": endpoints})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()

    return render(request, "auth/signup.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    
    return render(request, "auth/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
