from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import createUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url = 'orm-login')
def dashboard(request):
    return render(request,'orm/dashboard.html')

@unauthenticated_user
def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username, password= password)
        
        if user is not None:
            login(request,user)
            return redirect('orm-dashboard')
        else:
           messages.info(request, 'Username OR password is incorrect')

    return render(request,'orm/login.html')

def logoutuser(request):
    logout(request)
    return redirect("orm-login")

@unauthenticated_user
def register(request):
    form  = createUserForm()


    if request.method == 'POST':
        form =  createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="applicant")
            user.groups.add(group)
            name = form.cleaned_data.get("username")
            messages.success(request,'Account is cerated for '+name)
            return redirect("orm-login")
    context = {"form":form}
    return render(request,'orm/register.html',context)

@unauthenticated_user
def home(request):
    return render(request,'orm/home.html')