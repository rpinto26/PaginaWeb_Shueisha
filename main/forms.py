from django import forms
from . models import Blog, Noticias
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Formulario para crear un blog
class BlogCreate(forms.ModelForm):
   class Meta:
       model = Noticias
       fields = ["name","author","description","body","image"] 

#Formiario para login,logout
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']