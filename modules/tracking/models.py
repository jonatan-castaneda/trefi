from django.db import models
#from modules.users.models import User #Modelo de usuario default Django
from django.conf import settings

CUENTAS = {
    ("ING","Ingreso"),
    ("GTO","Gasto"),
    ("EFE","Efectivo"),
    ("MTA","Meta"),
}

TRANSACCIONES = {
    ("ING","Ingreso"),
    ("GTO","Gasto"),
    ("TRA","Traspaso"),
}


class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    clase_cuenta = models.CharField(max_length=100,choices=CUENTAS)
    nombre = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=9,decimal_places=2)
    saldo = models.DecimalField(max_digits=9,decimal_places=2)
    #usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Transaccion(models.Model):
    id = models.AutoField(primary_key=True)
    clase_trans =  models.CharField(max_length=100,choices=TRANSACCIONES)
    de_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,related_name='cuenta_origen')
    a_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,related_name='cuenta_destino')
    cantidad = models.DecimalField(max_digits=9,decimal_places=2)
    fecha = models.DateField(null=True)
    notas = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
