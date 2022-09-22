from django.contrib import admin
from . models import (Blog, Noticias, Reviews)
# Register your models here.

#En esta seccion vamos a registrar todos nuestros modelos 
#Para poder editarlos desde la administracion de DJANGO


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('articulo','nombre','texto')

@admin.register(Noticias)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

