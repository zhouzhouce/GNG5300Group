from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .utils import calculate_calories_duration
from . import models


def loginPage(request):
    context = {}
    if request.method == 'GET':
        return render(request, "login/login.html", context=context)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

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
                return redirect('/index/')

            else:
                messages.info(request, "Username OR Password is not correct.")
                return render(request, "login/login.html", context=context)


def index(request):
    context = {}
    if request.method == "POST":
        return redirect('videoDetails')
    if request.method == "GET":
        user = request.user
        training_level = models.UserProfile.objects.values("level").filter(user_id=user.id)
        titles = models.Exercise.objects.values("exercise_title").filter(level=training_level[0]["level"])
        sum_calories, sum_hours = calculate_calories_duration(request.user.id)

        context = {"level": training_level[0]["level"], "titles": titles, "title1": titles[0]["exercise_title"], "title2": titles[1]["exercise_title"],
                   "title3": titles[2]["exercise_title"], "sum_calories": sum_calories, "sum_hours": sum_hours}
        return render(request, 'login/index.html', context)


def select(request):
    context = {}
    if request.method == "POST":
        user = request.user
        return render(request, 'login/index.html')
    if request.method == "GET":
        return render(request, 'login/select.html', context)


def homepage(request):
    if request.method == 'GET':
        return render(request, "login/homepage.html")
    if request.method == 'POST':
        return redirect('/login/')


def videoDetails(request):
    pass
    return render(request, 'login/video_detail.html')

