#Importamos las librerias necesarias 

from django.urls import path
from . import views 
from main.views import comentarios

#llamamos a nuestra aplicaciones para heredar las views de la mismoa
app_name = "main"

urlpatterns = [

#Definimos todas las URLS
	path('', views.IndexView.as_view(), name="Home"),
	path('reviews/', views.BlogsView.as_view(), name="Blog"),
	path('blogs/', views.NoticiasView.as_view(), name="Blogs"),
	path('comentario/', views.comentarios),
	path('CrearReviews/', views.CrearRe, name="Crear"),
	path('login/', views.loginPage, name="login"),
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	


]