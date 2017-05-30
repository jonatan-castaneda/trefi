from django import forms
from django.forms import  ModelForm
from .models import CATEGORIA

class CursosForm(forms.Form):
    curso = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                "class":"form-control",
            }
        ),
        choices=CATEGORIA,
    )