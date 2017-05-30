from django.contrib import admin
from .models import Cuenta, Transaccion

# Register your models here.

class CuentaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cuenta, CuentaAdmin)

class TransaccionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Transaccion, TransaccionAdmin)
