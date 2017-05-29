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

TIPO_CUENTAS = {
    ("CAR","Cartera"),
    ("BAN","Cuenta Bancaria"),
    ("TDC","Tarjeta de Crédito"),
    ("NOM","Cuenta de Nómina"),
    ("AHO","Cuenta de Ahorro"),
    ("INV","Cuenta de Inversiones"),
    ("OTR","Otro"),
    ("SAL","Salario"),
    ("HON","Honorarios"),
    ("REN","Rendimiento inversiones"),
    ("APU","Apuestas"),
    ("ALI","Alimentos"),
    ("ENT","Entretenimiento"),
    ("DEP","Deporte"),
    ("ACC","Accesorios"),
    ("ROP","Ropa"),
    ("VID","Videojuegos"),
}

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    clase_cuenta = models.CharField(null=True,max_length=100,choices=CUENTAS)
    tipo_cuenta = models.CharField(null=True,max_length=100,choices=TIPO_CUENTAS)
    nombre = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=9,decimal_places=2)
    saldo = models.DecimalField(max_digits=9,decimal_places=2,default=0)
    #usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return "Cuenta: %s por %s" % (self.clase_cuenta,self.tipo_cuenta)

class Transaccion(models.Model):
    id = models.AutoField(primary_key=True)
    clase_trans =  models.CharField(max_length=100,choices=TRANSACCIONES)
    de_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,related_name='cuenta_origen')
    a_cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE,related_name='cuenta_destino')
    cantidad = models.DecimalField(max_digits=9,decimal_places=2)
    fecha = models.DateField(null=True)
    notas = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return "Transaccion: %s" % self.clase_trans
