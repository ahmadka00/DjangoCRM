from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # Check to see of logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        
    return render(request, 'website/home.html', {})


def logout_user(request):
    pass