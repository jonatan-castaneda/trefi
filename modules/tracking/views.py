from django.shortcuts import render, redirect
from .forms import CuentaForm, TransaccionForm, TicketForm
from modules.users.models import User
from .models import Cuenta, Transaccion, TRANSACCIONES, TIPO_CUENTAS, Ticket
from .functions import Saldos
from .gvision import getInformacion

# Create your views here.

def agregarCuenta(request):
        if request.method=="POST":
            print("En Post")
            form = CuentaForm(request.POST or None)
            if form.is_valid():
                cuenta = form.save()
                request.user.cuentas.add(cuenta)
                return redirect("landing:dashboard")
        else:
            form = CuentaForm()
            return render(request,'dashboard/cuenta.html',{'form':form})

def agregarTransaccion(request):
        if request.method=="POST":
            print("En Post")
            form = TransaccionForm(request.POST or None)
            if form.is_valid():
                trans = form.save(commit=False)
                trans.usuario = request.user #duda en si se requiere solicitar user
                trans.save()
                Saldos(trans.clase_trans,trans.cantidad,trans.de_cuenta.id,trans.a_cuenta.id)
                print(trans.de_cuenta.id,trans.a_cuenta.id,trans.clase_trans)
                return redirect("landing:dashboard")
        else:
            ticket_form = TicketForm()
            form = TransaccionForm()
            print(form)
            return render(request,'dashboard/transaccion.html',{'form':form, 'form_ticket':ticket_form})

def misTransacciones(request):
    transacciones = Transaccion.objects.filter(usuario=request.user)
    return render(request, "dashboard/transacciones.html",
        {
        'transacciones':transacciones,
        'transdict':dict(TRANSACCIONES)
        })

def misCuentas(request):
    cuentas = request.user.cuentas.all()
    print(cuentas)
    return render(request, "dashboard/cuentas.html",
    {
    'cuentas':cuentas,
    'cuendict':dict(TIPO_CUENTAS)
    })

def subirTicket(request):
    if request.method=="POST":
            form = TicketForm(request.POST, request.FILES)
            if form.is_valid():
                imagen = form.save(commit=False)
                imagen.usuario = request.user
                imagen.save()
                ticket = getInformacion("/media/%s" % (imagen.imagen))
                print(imagen.imagen)
                ticket_form = TicketForm()
                form.cleaned_data['fecha'] = ticket['fecha']
                form.cleaned_data['notas'] = ticket['descripcion']
                form.cleaned_data['cantidad'] = ticket['total']
                return render(request, "dashboard/transaccion.html",{'form':form, 'form_ticket':ticket_form})
            else:
                return redirect("landing:dashboard")
