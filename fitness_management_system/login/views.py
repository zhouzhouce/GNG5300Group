from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .utils import calculate_calories_duration, generate_event_data
import datetime
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
        title = request.POST.get("title")
        link = models.Exercise.objects.values("link").filter(exercise_title=title)[0]["link"]
        exercise_id = models.Exercise.objects.values("id").filter(exercise_title=title)[0]["id"]
        d = datetime.date.today()
        event = models.EventData.objects.filter(user_id=request.user.id, exercise_id=exercise_id, created_at=d)
        if not event:
            models.EventData.objects.create(user_id=request.user.id, exercise_id=exercise_id, created_at=d, exercise_times=1)
        else:
            exercise_times = \
            models.EventData.objects.values("exercise_times").filter(user_id=request.user.id, exercise_id=exercise_id,
                                                                     created_at=d)[0]["exercise_times"]
            models.EventData.objects.filter(user_id=request.user.id, exercise_id=exercise_id).update(exercise_times=exercise_times+1)

        context['video_link'] = link
        return render(request, 'login/video_detail.html', context=context)
    if request.method == "GET":
        user = request.user
        training_level = models.UserProfile.objects.values("level").filter(user_id=user.id)
        titles = models.Exercise.objects.values("exercise_title").filter(level=training_level[0]["level"])
        durations = models.Exercise.objects.values("duration").filter(level=training_level[0]["level"])
        sum_calories, sum_hours = calculate_calories_duration(request.user.id)

        context = {"level": training_level[0]["level"], "titles": titles, "title1": titles[0]["exercise_title"],
                   "title2": titles[1]["exercise_title"], "title3": titles[2]["exercise_title"],
                   "sum_calories": sum_calories, "sum_hours": sum_hours, "duration1": durations[0]["duration"],
                   "duration2": durations[1]["duration"], "duration3": durations[2]["duration"]}
        return render(request, 'login/index.html', context)


def select(request):
    if request.method == "POST":
        user_email = request.user
        user_id = User.objects.values("id").filter(email=user_email)

        username = request.POST.get("username")
        gender = request.POST.get("gender")
        training_level = request.POST.get("training level")

        models.UserProfile.objects.create(name=username, user_id=user_id, gender=gender, level=training_level)
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
    if request.method == 'GET':
        return render(request, 'login/video_detail.html')

