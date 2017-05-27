from django.shortcuts import render
from .forms import CuentaForm, TransaccionForm
from django.contrib.auth.models import User
from .models import Cuenta, Transaccion

# Create your views here.

def agregarCuenta(request):
        if request.method=="POST":
        print("En Post")
        form = CuentaForm(request.POST or None)
        if form.is_valid():
            cuenta = form.save(commit=False)
            cuenta.usuario = request.user #duda en si se requiere solicitar user
            cuenta.save()
            User.cuentas = cuenta
            User.save
            return redirect("landing:dashboard")
    else:
        form = CuentaForm()
        return render(request,'dashboard/index.html',{'form':form}) #duda en url

def agregarTransaccion(request):
        if request.method=="POST":
        print("En Post")
        form = TransaccionForm(request.POST or None)
        if form.is_valid():
            trans = form.save(commit=False)
            trans.usuario = request.user #duda en si se requiere solicitar user
            trans.save()
            return redirect("landing:dashboard")
    else:
        form = TransaccionForm()
        return render(request,'dashboard/index.html',{'form':form}) #duda en url
