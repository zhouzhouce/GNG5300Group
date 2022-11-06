import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from login import models


def loginPage(request):
    context = {}
    if request.method == 'GET':
        return render(request, "login/login.html", context=context)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = models.User.objects.get(email=email)

        if not user_obj:
            models.User.objects.create(email=email, password=password)
            messages.info(request, "new user has been registered.")
            return redirect('/index/')
        else:
            user_obj = models.User.objects.filter(email=email, password=password)
            if user_obj:
                return redirect('/index/')
            else:
                messages.error(request, "Username OR Password is not correct.")
                return render(request, "login/login.html", context=context)


def index(request):
    pass
    return render(request, 'login/index.html')


@api_view(['GET', 'POST'])
def verifyApi(request):
    if request.method == 'GET':
        return JsonResponse({'code': 500, 'message': "please input your account and password"})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.User.objects.filter(email=username, password=password)
        if user_obj:
            return JsonResponse({'code': 200, 'message': "succeed"})
        return JsonResponse({'code': 200})


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
