from django.shortcuts import render
from .models import Contenido, CATEGORIA, TEMA
import json

# Create your views here.

def index(request):
    contenido = Contenido.objects.all()
    categ = dict(CATEGORIA)
    tem = dict(TEMA)
    return render(request, "educacion/index.html",{
        'contenido':contenido,
        'categoria':categ,
        'tema':tem,
    })

def contenido(request, pk=0):
    if pk == 0:
        contenido = Contenido.objects.all()
        contenido = Contenido.objects.get(id=pk)
        return render(request, "educacion/index.html",{
            'contenido':contenido
        })
    else:
        contenido = Contenido.objects.get(id=pk)
        categ = dict(CATEGORIA)
        tem = dict(TEMA)
        return render(request, "educacion/contenido.html",{
            'categoria':categ.get(contenido.categoria),
            'tema':tem.get(contenido.tema),
            'categorias':categ,
            'contenido':contenido,
        })

def contenido_categoria(request, pk=""):
    if pk == "":
        return index(request)
    else:
        categ = dict(CATEGORIA)
        tem = dict(TEMA)
        try:
            contenido = Contenido.objects.filter(categoria = pk)
            return render(request, "educacion/index.html",{
            'contenido':contenido,
            'categoria':categ,
            'tema':tem,
            })
        except:
            return index(request)

def contenido_busqueda(request):
    if request.method == "GET":
        q = request.GET['q']
        categ = dict(CATEGORIA)
        tem = dict(TEMA)
        try:
            contenido = Contenido.objects.filter(resumen__content = q)
            return render(request, "educacion/index.html",{
            'contenido':contenido,
            'categoria':categ,
            'tema':tem,
            })
        except:
            return index(request)
    else:
        return index(request)

