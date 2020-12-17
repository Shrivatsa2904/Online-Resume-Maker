from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import createUserForm,personinfo,educationFormset,projectFormset,internshipFormset,technicalinfo,certificateFormset
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url = 'orm-login')
def dashboard(request):
    form = personinfo()
    educationform = educationFormset()
    projectform = projectFormset()
    internshipform = internshipFormset()
    certificateform = certificateFormset()
    technicalform = technicalinfo()
    if request.method == 'POST':
        form = personinfo(request.POST)
        educationform = educationFormset(request.POST)
        projectform = projectFormset(request.POST)
        internshipform = internshipFormset(request.POST)
        certificateform = certificateFormset(request.POST)
        technicalform = technicalinfo(request.POST)
        print("vatsa not valid")
        if  form.is_valid():
            print("vatsa valid")
            name = educationform
            new_resume_item = form.save(commit=False)
            new_resume_item.user = request.user
            new_resume_item.save()
            return render(request, 'orm/samples.html', {'form':name })
    print("fail")
    return render(request, 'orm/dashboard.html', {'form': form,'edform':educationform,'proform':projectform,
    'intform':internshipform,'certform': certificateform,'techform':technicalform})
   
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


def samplepage(request):
    return render(request,'orm/samples.html')

