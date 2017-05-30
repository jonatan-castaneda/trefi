from django.shortcuts import render
from .models import Contenido

# Create your views here.

def index(request):
    contenido = Contenido.objects.all()
    return render(request, "educacion/index.html",{
        'contenido':contenido,
    })

def curso(request):
    return render(request, "educacion/curso.html")
