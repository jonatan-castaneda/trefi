from django.conf.urls import url
from .views import agregarTransaccion, agregarCuenta

urlpatterns = [
    url(r'^transaccion/$', agregarTransaccion, name="transaccion"),
]
