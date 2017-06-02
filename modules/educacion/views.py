from django.shortcuts import render, redirect
from .models import Contenido, CATEGORIA, TEMA, Curso, TrackingEducacion

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
            return redirect("educacion:index")

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
            return redirect("educacion:index")
    else:
        return redirect("educacion:index")

def cursos(request):
    try:
        categ = dict(CATEGORIA)
        cursos = TrackingEducacion.objects.filter(usuario = request.user)
        return render(request, "educacion/curso.html", {
            'categoria':categ,
            'cursos':cursos,
        })
    except:
        return render(request,"educacion/curso.html", {
            'sin_cursos':"Aún no tienes cursos registrados",
        })
    #except:
    #    return redirect("educacion:index")

def cursos_agregar(request, pk=0):
    cursos = Curso.objects.all()
    return render(request, "educacion/add_cursos.html",{
        'cursos':cursos,
    })

def cursos_registrar(request, pk=0):
    try:
        print(pk)
        curso = TrackingEducacion()
        curso.usuario = request.user
        curso.curso = Curso.objects.get(id=pk)
        curso.save()
        return redirect("educacion:cursos")
    except:
        return redirect("educacion:cursos")

def cursos_eliminar(request, pk=0):
    try:
        TrackingEducacion.objects.get(id=pk).delete()
        return redirect("educacion:cursos")
    except:
        return redirect("educacion:cursos")

def cursos_ver(request, pk=0):
    try:
        cursos_user = TrackingEducacion.objects.get(id = pk)
        categ = dict(CATEGORIA)
        tem = dict(TEMA)
        return render(request, "educacion/ver_curso.html",{
            'categoria':categ,
            'tema':tem,
            'cursos':cursos_user.curso.contenidos.all(),
        })
    except:
        return redirect("educacion:cursos")