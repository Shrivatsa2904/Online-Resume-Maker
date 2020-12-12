from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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