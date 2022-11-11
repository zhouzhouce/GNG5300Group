from django.shortcuts import render, redirect
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

            return redirect('/select/')

        else:
            user_obj = User.objects.filter(email=email, password=password)
            if user_obj:
                user_obj = User.objects.get(email=email, password=password)
                login(request, user_obj)
                return redirect('/select/')

            else:
                messages.info(request, "Username OR Password is not correct.")
                return render(request, "login/login.html", context=context)


def index(request):
    pass
    return render(request, 'login/index.html')


def select(request):
    if request.method == "POST":
        user_email=request.user
        user_id= User.objects.values("id").filter(email=user_email)

        username=request.POST.get("username")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        training_level=request.POST.get("training level")
#create
        models.UserProfile.objects.create(name=username,user_id=user_id,gender=gender,level=training_level)
        User.objects.filter(email=user_email).update(username=username)
        return redirect('/index/')
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

