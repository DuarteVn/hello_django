from django.shortcuts import render, redirect
from app_wpp.models import evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages                           

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
    # def index(request):
#     return redirect("/home/")

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    Evento = evento.objects.filter(usuario=usuario)
    # usuario = request.user
    # Evento = evento.objects.filter(usuario=usuario)
    dados = {'eventos':Evento} 
    return render(request, 'home.html', dados)

@login_required(login_url='/login/')
def Evento(request):
    return render(request, 'evento.html')