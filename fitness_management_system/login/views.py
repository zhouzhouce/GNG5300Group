from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
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
        events = models.EventData.objects.filter(user_id=request.user.id)
        sum_calories = 0
        sum_hours = 0

        for i in range(0, len(events)):
            times = models.EventData.objects.values("exercise_times").filter(user_id=request.user.id)[i]["exercise_times"]
            exercise_id = models.EventData.objects.values("exercise_id").filter(user_id=request.user.id)[i]["exercise_id"]
            calories = models.Exercise.objects.values("calories").filter(id=exercise_id)[0]["calories"] * times
            hours = models.Exercise.objects.values("duration").filter(id=exercise_id)[0]["duration"] * times

            sum_calories = sum_calories + calories
            sum_hours = sum_hours + hours

        context = {"levels": training_level, "titles": titles, "sum_calories": sum_calories, "sum_hours": sum_hours}
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

