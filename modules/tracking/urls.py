from django.conf.urls import url
from .views import agregarTransaccion, agregarCuenta, misTransacciones,misCuentas

urlpatterns = [
    url(r'^transaccion/$', agregarTransaccion, name="transaccion"),
    url(r'^nuevacuenta/$', agregarCuenta, name="cuenta"),
    url(r'^transacciones/$', misTransacciones, name="transacciones"),
    url(r'^cuentas/$', misCuentas, name="cuentas"),
]
