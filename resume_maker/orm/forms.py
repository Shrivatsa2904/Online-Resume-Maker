from django.forms import ModelForm,formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import persondetails,education,projects,internships,certifications,technical
class createUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-field','placeholder': 'Password','required':'required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-field','placeholder': 'Confirm Password','required':'required'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username' : forms.TextInput(attrs = {'class':'input-field','placeholder': ' Username','required':'required'}),
            'email' : forms.TextInput(attrs = {'class':'input-field','placeholder': 'Email','required':'required'}),
        }

class personinfo(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Full Name ex.,Darshan DR','required':'required','label':'Your Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Email','required':'required'}))
    linkedin = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'LinkedIn url ex.,https://www.linkedin.com/in/profile-name'}))
    github = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Github url'}))
    dob = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'dd/mm/yyyy'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Address'}))
    father = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Father Name'}))

    class Meta:
        model = persondetails
        fields = ['name','phone','email','linkedin','github','dob','address','father','summary']
        widgets = {
            'summary' : forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Description',"padding":'100px'}),
            'phone' :   forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Phone number','required':'required'})
        }

class educationinfo(forms.ModelForm):
    name = forms.CharField(label='Instituion Name',widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'College or School name ex.,BNMIT','required':'required',}))
    start = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex.,16/08/2017',}))
    end = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., 21/07/2021 or present'}))
    score= forms.CharField(label='CGPA/Percentage',widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., cgpa 8.5 or percentage 88%','required':'required'}))
    subject = forms.CharField(label='Branch or Subject combination',widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Subjects studied or branch ex., PCMB or Information Science'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., Bangalore'}))

    class Meta:
        model = education
        fields = ['name','start','end','score','subject','location']

educationFormset = formset_factory(educationinfo, extra=1)


class projectinfo(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., Online Resume Builder','required':'required'}))
    tech = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., Django, Html, CSS'}))
   

    class Meta:
        model = projects
        fields = ['title','tech','description']
        widgets = {
            'description' : forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Description'})
        }


projectFormset = formset_factory(projectinfo, extra=1)

class internshipinfo(forms.ModelForm):
    company = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., BNMIT','required':'required'}))
    start = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., 16/06/2017','required':'required'}))
    to = forms.CharField(label='end',widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., 16/08/2017 or Present','required':'required'}))
   

    class Meta:
        model = internships
        fields = ['company','start','to','description']
        widgets = {
            'description' : forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'Description'})
        }

internshipFormset = formset_factory(internshipinfo, extra=1)

class certificateinfo(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., Deep Learning Specialization','required':'required'}))
    source = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., Coursera','required':'required'}))
   

    class Meta:
        model = certifications
        fields = ['title','source']

certificateFormset = formset_factory(certificateinfo, extra=1)

class technicalinfo(forms.ModelForm):
    languages = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., Java, PythonS'}))
    tools = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., Microsoft word, SQL, CAD'}))
    familiar = forms.CharField(widget=forms.TextInput(attrs={'oninput':"this.className = ''",'placeholder': 'ex., Machine Learning'}))
   

    class Meta:
        model = technical
        fields = ['languages','tools','familiar']