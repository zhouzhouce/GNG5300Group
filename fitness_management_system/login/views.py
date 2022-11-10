from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models


def loginPage(request):
    context = {}
    if request.method == 'GET':
        return render(request, "login/login.html", context=context)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is None or password is None:
            return render(request, "login/login.html", context=context)
        user_obj = User.objects.filter(email=email)

        if not user_obj:
            User.objects.create(username=email, email=email, password=password)
            messages.info(request, "New user has been registered.")
            user_obj = User.objects.get(email=email, password=password)
            login(request, user_obj)
            return redirect('/index/')
        else:
            user_obj = User.objects.filter(email=email, password=password)
            if user_obj:
                user_obj = User.objects.get(email=email, password=password)
                login(request, user_obj)
                return redirect('/index/')
            else:
                messages.info(request, "Username OR Password is not correct.")
                return render(request, "login/login.html", context=context)


def index(request):
    pass
    return render(request, 'login/index.html')


def select(request):
    if request.method == "POST":
        print(request.POST.get("Age"))
        # print(request.POST.get("password"))
        return render(request, 'login/select.html')
    if request.method == "GET":
        return render(request, 'login/select.html')


def homepage(request):
    if request.method == 'GET':
        return render(request, "login/homepage.html")
    if request.method == 'POST':
        return redirect('/login/')


def videoDetails(request):
    pass
    return render(request, 'login/video_detail.html')
