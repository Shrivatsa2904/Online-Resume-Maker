from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

def home(request):
    return render(request,'orm/home.html')

def login(request):
    return render(request,'orm/login.html')

def register(request):
    return render(request,'orm/register.html')