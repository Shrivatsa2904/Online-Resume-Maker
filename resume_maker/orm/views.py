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
from .models import education
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa

# Create your views here.
@login_required(login_url = 'orm-login')
def dashboard(request):
    form = personinfo()
    educationform = educationFormset()
    projectform = projectFormset()
    internshipform = internshipFormset()
   
    technicalform = technicalinfo()
    if request.method == 'POST':
        form = personinfo(request.POST)
        educationform = educationFormset(request.POST)
        print("vatsa not valid")
        if  form.is_valid() and educationform.is_valid():
            print("vatsa valid")
            educations = educationform.cleaned_data
            new_resume_item = form.save(commit=False)
            new_resume_item.user = request.user
            new_resume_item.save()
            for f in educationform:
                a = f.save(commit=False)
                a.user = request.user
                a.save()
            name = form.cleaned_data
            education(name=name,user = request.user).save()
            request.session['personalinfo'] = name
            request.session['educationinfo'] = educations
            return  redirect(projectview)
    print("fail")
    return render(request, 'orm/dashboard.html', {'form': form,'edform':educationform})

@login_required(login_url = 'orm-login')
def projectview(request):
    projectform = projectFormset()
    if request.method == 'POST':
        projectform = projectFormset(request.POST)
        if  projectform.is_valid():
            for f in projectform:
                a = f.save(commit=False)
                a.user = request.user
                a.save()
            project = projectform.cleaned_data
            request.session['projectinfo'] = project
            return  redirect(internshipview)
    return render(request, 'orm/samples.html', {'proform':projectform})

@login_required(login_url = 'orm-login')
def internshipview(request):
    internshipform = internshipFormset()
    if request.method == 'POST':
        internshipform =  internshipFormset(request.POST)
        if  internshipform.is_valid():
            for f in internshipform:
                a = f.save(commit=False)
                a.user = request.user
                a.save()
            internship = internshipform.cleaned_data
            request.session['internshipinfo'] = internship
            return  redirect(certificateview)

    return render(request, 'orm/internship.html', {'intform':internshipform})

@login_required(login_url = 'orm-login')
def certificateview(request):
    certificateform = certificateFormset()
    tech = technicalinfo
    if request.method == 'POST':
        certificateform =  certificateFormset(request.POST)
        tech = technicalinfo(request.POST)
        if   certificateform.is_valid() and tech.is_valid():
            for f in certificateform:
                a = f.save(commit=False)
                a.user = request.user
                a.save()
            t = tech.save(commit=False)
            t.user = request.user
            t.save()
            certificate =  certificateform.cleaned_data
            technical = tech.cleaned_data
            request.session['certificateinfo'] =  certificate
            request.session['technicalinfo'] =  technical
            return  redirect(choiceview)

    return render(request, 'orm/certificate.html', {'certform':certificateform,'techform':tech })

@login_required(login_url = 'orm-login')
def choiceview(request):
    if request.method == 'POST':
        if 'resume1' in request.POST:
            return  redirect(render_pdf1)
        
        if 'resume2'  in request.POST:
             return  redirect(render_pdf2)

        if 'resume3'  in request.POST:
             return  redirect(render_pdf3)


    return render(request, 'orm/choice.html')

def render_pdf1(request):
    path = "orm/resume1.html"
    context = {'internship':request.session['internshipinfo'],
            'personal': request.session['personalinfo'],'education':request.session['educationinfo'],
            'certificate':request.session['certificateinfo'],'tech': request.session['technicalinfo'],'project': request.session['projectinfo']}

    html = render_to_string('orm/resume1.html',context)
    io_bytes = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
    if not pdf.err:
        return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error while rendering PDF", status=400)


def render_pdf2(request):
    path = "orm/resume2.html"
    context = {'internship':request.session['internshipinfo'],
            'personal': request.session['personalinfo'],'education':request.session['educationinfo'],
            'certificate':request.session['certificateinfo'],'tech': request.session['technicalinfo'],'project': request.session['projectinfo']}
    html = render_to_string('orm/resume2.html',context)
    io_bytes = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
    if not pdf.err:
        return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error while rendering PDF", status=400)

def render_pdf3(request):
    path = "orm/resume3.html"
    context = {'internship':request.session['internshipinfo'],
            'personal': request.session['personalinfo'],'education':request.session['educationinfo'],
            'certificate':request.session['certificateinfo'],'tech': request.session['technicalinfo'],'project': request.session['projectinfo']}
    html = render_to_string('orm/resume3.html',context)
    io_bytes = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
    if not pdf.err:
        return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error while rendering PDF", status=400)


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




