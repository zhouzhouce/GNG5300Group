import json
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from login import models


def loginPage(request):
    if request.method == 'GET':
        return render(request, "login/login.html")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = models.User.objects.filter(email=email, password=password)
        if user_obj:
            # return JsonResponse({'code': 200, 'message': "succeed"})
            return render(request, "login/index.html")
        else:
            return render(request, "login/login.html")


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
