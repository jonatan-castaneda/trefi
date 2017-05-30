from django import forms
from django.forms import  ModelForm
from .models import Cuenta, Transaccion, TRANSACCIONES, CUENTAS, TIPO_CUENTAS
#Son solo dos forms, uno para las cuentas (efectivo, ingreso y gasto) y otro para las transacciones (ingreso,gasto)
'''
class CuentaForm(forms.Form):
    clase_cuenta = forms.CharField(max_length=100,widget=forms.Select(
        attrs={
            "class":"form-control",
            "placeholder":"clase_cuenta"
        }
    ))
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"nombre"
        }
    ))
    presupuesto = forms.IntegerField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"presupuesto"
        }
    ))

class TransaccionForm(forms.Form):
    OPTIONS = [
    "1","2","3"
    ]

    clase_trans = forms.ChoiceField(choices=TRANSACCIONES,widget=forms.Select(
        attrs={
            "class":"form-control",
            "placeholder":"clase_trans"
        }

    ))
    de_cuenta = forms.CharField(max_length=100,widget=forms.Select(
        attrs={
            "class":"form-control",
            "placeholder":"de_cuenta"
        }
    ))
    a_cuenta = forms.CharField(max_length=100,widget=forms.Select(
        attrs={
            "class":"form-control",
            "placeholder":"a_cuenta"
        }
    ))
    cantidad = forms.IntegerField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"presupuesto"
        }
    ))
    fecha = forms.DateField(widget=forms.DateInput(
        attrs={
            "class":"form-control",
            "placeholder":"fecha"
        }
    ))
    notas = forms.CharField(widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"notas"
        }
    ))
'''

class CuentaForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(CuentaForm,self).__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    class Meta:
        model = Cuenta
        fields = ('clase_cuenta','tipo_cuenta','nombre','presupuesto')
        widget = {
            'clase_cuenta': forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':"clase_cuenta"
                }
            )
        }

class TransaccionForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(TransaccionForm,self).__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

    class Meta:
        model = Transaccion
        fields = ('clase_trans','de_cuenta','a_cuenta','cantidad','fecha','notas')
        widget = {
            'clase_trans': forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'clase_trans'
                }
            )
        }
