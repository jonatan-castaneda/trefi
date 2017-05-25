from django import forms
from django.forms import  ModelForm

#Son solo dos forms, uno para las cuentas (efectivo, ingreso y gasto) y otro para las transacciones (ingreso,gasto)

class CuentaForm(forms.Form):
    tipo_cuenta = forms.CharField(max_length=100,widget=forms.ChoiceField(
        attrs={
            "class":"form-control",
            "placeholder":"tipo_cuenta"
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

class Ingreso(forms.Form):
    de_cuenta = forms.CharField(max_length=100,widget=forms.ChoiceField(
        attrs={
            "class":"form-control",
            "placeholder":"de_cuenta"
        }
    ))
    a_cuenta = forms.CharField(max_length=100,widget=forms.ChoiceInput(
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
    notas = forms.TextField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"notas"
        }
    ))
