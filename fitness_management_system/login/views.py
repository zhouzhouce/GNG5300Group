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

        try:
            user_obj = models.User.object.get(email=email)
        except:
            messages.error(request, "User doesn't exist.")

        user_obj = models.User.objects.filter(email=email, password=password)
        if user_obj:
            return render(request, "login/index.html", context=context)
            # return JsonResponse({'code': 200, 'message': "succeed"})
        else:
            messages.error(request, "Username OR Password is not correct.")
            return render(request, "login/login.html", context=context)


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



