#Importamos las librerias necesarias 

from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

#Creamos una tabla de BLOGS
class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Obras'
        verbose_name = 'Obra'
        ordering = ["timestamp"]

#Agregamos los campos y sus tipos de datos

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


#Tabla de Reviews(Comentarios)
class Reviews(models.Model):

    #Campos con su tipo de dato
    nombre = models.CharField(max_length=30) #CharField se traduce como Varchar
    texto = RichTextField()
    articulo = models.CharField(max_length=200) 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        texto1 = "{0} ({1})"
        return texto1.format(self.nombre, self.texto)


#Tabla de noticias
class Noticias(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    #Campos con su tipo de dato
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="noticias")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Noticias, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


    

    
