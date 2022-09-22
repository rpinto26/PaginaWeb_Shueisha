
#IMPORTAMOS LIBRERIAS DE DJANGO Y OTRAS
 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

#IMPORTAMOS LOS MODELOS

from main.forms import BlogCreate, CreateUserForm
from .models import (
		Blog,
		Noticias,
		Reviews,
	)

# Create your views here.


#Funcion para la pagina de registro
def registerPage(request):
	if request.user.is_authenticated: #Si el usuario esta autenticado
		return redirect('main:Home') #redireccionamos a la pagina principal
	else: #Sino Creamos el usuario si el formulario esta correcto
		form = CreateUserForm() 
		if request.method == "POST":
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was craeted for')

				return redirect('main:Home')
		context = {'form':form}
		return render(request, 'main/register.html', context)


#Funcion Para el Inicio de Sesion
def loginPage(request):
	if request.user.is_authenticated:  #Si el usuario esta autenticado redireccionamos a la pagina principal
		return redirect('/')
	else:  #Sino, intentamos Iniciar sesion con las credenciales recibidas
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)
			
			if user is not None:  
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username or password incorrect') #Sino las credenciales recibidas son incorrectas

		context = {}
		return render(request, 'main/login.html', context)

# Funcion Para cerrar sesion
def logoutUser(request):
	logout(request)
	return redirect('/')  #Al cerrar sesion redirecciona a la pagina principal

# Login required para solicitarle al usuario que se registre para realizar algunas funciones especiales 
@login_required(login_url='/login')
def CrearRe(request):
	form = None
	if request.method=="POST":
		form = BlogCreate(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	return render(request, "main/CrearRe.html",{"form":form})
		

#Funcion para poder añadir comentarios
def comentarios(request):
	Nombre = request.POST['nombre']
	Comen = request.POST['revi']
	articulo = request.POST['articulo']
	
	#Sentencia SQL para crear un dato de una tabla
	RE = Reviews.objects.create(nombre = Nombre, texto=Comen, articulo=articulo)
	return redirect('/reviews?mensaje=EXITO')


#Clase De la vista del models de Index
class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		blogs = Noticias.objects.filter(is_active=True)
		reviews = Reviews.objects.filter(is_active=True)
		context["blogs"] = blogs
		return context

#Clase De la vista del models de Blogs
class BlogsView(generic.TemplateView):
	template_name = "main/reviews.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		blogs = Blog.objects.all()
		reviews = Reviews.objects.filter(is_active=True)
		context["blogs"] = blogs
		context["reviews"] = reviews
		return context

#Se hizo un registro para filtrar los comentarios segun el titulo del manga
@register.filter
def filtrar(titulo):
	return Reviews.objects.filter(articulo=titulo)

#Class Para mostrar las noticias
class NoticiasView(generic.TemplateView):
	template_name = "main/blog.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		blogs = Noticias.objects.all()
		reviews = Reviews.objects.filter(is_active=True)
		context["blogs"] = blogs
		context["reviews"] = reviews
		return context





		

















class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"