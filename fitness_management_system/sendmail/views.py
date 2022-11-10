import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from login import models
from django.core.mail import send_mail
from fitness_management_system import settings

# Create your views here.



