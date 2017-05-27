from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm
#from django.contrib.auth.models import User #Modelo de usuario default Django
from modules.users.models import User
from django.contrib.auth import authenticate,logout as logout_app,login as login_app #Pseudonimos para que no se confunda con el nombre de la funcion
from django.http import HttpResponse

def index(request):
    form_login = LoginForm(request.POST or None)
    form_signup = SignupForm(request.POST or None)
    return render(request, "landing/index.html", {
        "form_login":form_login,
        "form_signup":form_signup,
        })

def dashboard(request):
    return render(request, "dashboard/index.html")

#Tres funciones para autenticacion de usuario: Signup, Login y Logout
def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                )
            if user is not None:
                login_app(request,user)
                return redirect('landing:dashboard')
            else:
                return HttpResponse("Usuario no encontrado")

    return render(request,'landing/index.html', {"login":form})

def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data.pop('confirm_password', None)
            user = User.objects.create_user(**form.cleaned_data)
            return redirect("landing:dashboard")

    return render(request,'landing/index.html',{'sign':form})

def logout(request):
    logout_app(request)
    return redirect("landing:index")

