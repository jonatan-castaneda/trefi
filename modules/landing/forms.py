from django import forms
from django.forms import  ModelForm

class SignupForm(forms.Form):

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"email"
            }
        ))

    password  = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"password"
            }
        ))

    confirm_password  = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"confirm password"
            }
        ))

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class LoginForm(forms.Form):

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"email"
            }
        ))

    password  = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"password"
            }
        ))
