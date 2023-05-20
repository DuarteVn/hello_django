from django.shortcuts import render, redirect
from app_wpp.models import evento


def index(request):
    return redirect("/home/")


def lista_eventos(request):
    Evento = evento.objects.all()

    # usuario = request.user
    # Evento = evento.objects.filter(usuario=usuario)
    dados = {'eventos':Evento}
    return render(request, 'home.html', dados)

