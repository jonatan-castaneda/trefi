from django.db import models
from django.contrib.auth.models import User #Modelo de usuario default Django

CUENTAS = {
    ("CAR","Cartera"),
    ("BAN","Cuenta Bancaria"),
    ("TDC","Tarjeta de Crédito"),
    ("NOM","Cuenta de Nómina"),
    ("AHO","Cuenta de Ahorro"),
    ("INV","Cuenta de Inversiones"),
    ("OTR","Otro"),
}

INGRESOS = {
    ("SAL","Salario"),
    ("HON","Honorarios"),
    ("REN","Rendimiento inversiones"),
    ("APU","Apuestas"),
}

GASTOS = {
    ("ALI","Alimentos"),
    ("ENT","Entretenimiento"),
    ("DEP","Deporte"),
    ("ACC","Accesorios"),
    ("ROP","Ropa"),
    ("VID","Videojuegos"),
}


class CuentaEfectivo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=100,choices=CUENTAS)
    nombre = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=9,decimal_places=2)
    saldo = models.DecimalField(max_digits=9,decimal_places=2)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

class CuentaIngreso(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=100,choices=INGRESOS)
    nombre = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=9,decimal_places=2)
    saldo = models.DecimalField(max_digits=9,decimal_places=2)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

class CuentaGasto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=100,choices=GASTOS)
    nombre = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=9,decimal_places=2)
    saldo = models.DecimalField(max_digits=9,decimal_places=2)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)
    de_cuenta = models.ForeignKey(CuentaIngreso,on_delete=models.CASCADE)
    a_cuenta = models.ForeignKey(CuentaEfectivo,on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=9,decimal_places=2)
    fecha = models.DateField(null=True)
    notas = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

class Gasto(models.Model):
    id = models.AutoField(primary_key=True)
    de_cuenta = models.ForeignKey(CuentaEfectivo,on_delete=models.CASCADE)
    a_cuenta = models.ForeignKey(CuentaGasto,on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=9,decimal_places=2)
    fecha = models.DateField(null=True)
    notas = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
