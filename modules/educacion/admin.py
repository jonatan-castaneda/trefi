from django.contrib import admin
from django.db import models
from .models import Contenido, Curso, TrackingEducacion, CATEGORIA,TEMA

# Register your models here.
class ContenidoAdmin(admin.ModelAdmin):
    pass

class CursoAdmin(admin.ModelAdmin):
    pass

class TrackingEducacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contenido, ContenidoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(TrackingEducacion, TrackingEducacionAdmin)
