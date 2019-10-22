from django.shortcuts import render, redirect
from .models import Encontro, Presenca
from django.contrib.auth.decorators import login_required
from crismando.models import Crismando, Turma
# Create your views here.


@login_required
def encontroHome(request):
    return render(request,'encontro/encontroHome.html')


def listaPresenca(request):
    encontro = Encontro()
