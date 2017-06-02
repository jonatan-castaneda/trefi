from .models import Cuenta, Transaccion


def Saldos(clase_trans,importe,pk1,pk2):
    cuenta_origen = Cuenta.objects.get(id=pk1)
    cuenta_destino = Cuenta.objects.get(id=pk2)

    if clase_trans == "ING":
        cuenta_origen.saldo = cuenta_origen.saldo + importe
        cuenta_origen.save()
        cuenta_destino.saldo = cuenta_destino.saldo + importe
        cuenta_destino.save()
    else:
        cuenta_origen.saldo = cuenta_origen.saldo - importe
        cuenta_origen.save()
        cuenta_destino.saldo = cuenta_destino.saldo + importe
        cuenta_destino.save()

def Balance(user):
    bal = 0
    for cuenta in user.cuentas.all():
        if cuenta.clase_cuenta == 'EFE':
            bal += cuenta.saldo
    return bal

def SaldoIngresos(user):
    bal = 0
    for cuenta in user.cuentas.all():
        if cuenta.clase_cuenta == 'ING':
            bal += cuenta.saldo
    return bal

def SaldoGastos(user):
    bal = 0
    for cuenta in user.cuentas.all():
        if cuenta.clase_cuenta == 'GTO':
            bal += cuenta.saldo
    return bal

def SaldoMetas(user):
    bal = 0
    for cuenta in user.cuentas.all():
        if cuenta.clase_cuenta == 'MTA':
            bal += cuenta.saldo
    return bal

def TransLine():
    transacciones = []
    for trans in Transaccion.objects.all():
        dic = {'periodo':str(trans.fecha),'ingreso':str(trans.cantidad)}
        transacciones.append(dic)
    return transacciones

def BalanceChart(user):
    cuentas = []
    for cuenta in user.cuentas.filter(clase_cuenta="ING"):
        dic = {'label':str(cuenta.nombre),'value':str(cuenta.saldo)}
        cuentas.append(dic)
    return cuentas

def GastosChart(user):
    cuentas = []
    for cuenta in user.cuentas.filter(clase_cuenta="GTO"):
        dic = {'label':str(cuenta.nombre),'value':str(cuenta.saldo)}
        cuentas.append(dic)
    return cuentas
