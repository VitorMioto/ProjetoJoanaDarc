from django.shortcuts import render, redirect
from .models import Encontro, Presenca
from crismando.models import Crismando, Turma
# Create your views here.
def encontroHome(request):
    return render(request,'encontro/encontroHome.html')


def listaPresenca(request):
    encontro = Encontro()
