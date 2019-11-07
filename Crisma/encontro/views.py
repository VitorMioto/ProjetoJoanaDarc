from django.shortcuts import render, redirect
from .models import Encontro, Presenca
from django.contrib.auth.decorators import login_required
from crismando.models import Crismando, Turma
from datetime import datetime
# Create your views here.


@login_required
def encontroHome(request):
    return render(request,'encontro/encontroHome.html')


def listarEncontros(request):
    encontros = Encontro.objects.all.filter(registroPresenca='N')
    data = {'encontros': encontros}
    return render(request, 'encontro/listarEncontros.html',data)

def cadastrarEncontro(request):

    if request.POST:
        if request.POST['dtEncontro']=='' or request.POST['dtEncontro'] == None:
            data = {'errorMessage','Favor preencher a data do encontro.'}
            return render(request, 'encontro/cadastrarEncontro.html',data)
        elif request.POST['temaEncontro'] =='' or request.POST['temaEncontro'] == None:
            data = {'errorMessage', 'Favor preencher o tema do encontro.'}
            return render(request, 'encontro/cadastrarEncontro.html', data)
        elif request.POST['dtEncontro']!='' and request.POST != None:
            try:
                dtEncontro = datetime.strptime(request.POST['dtEncontro'],'%Y-%m-%d').date()
                encontro = Encontro.objects.all.filter(dtEncontro=dtEncontro)
                if encontro:
                    data = {'errorMessage':'Já registrado encontro nessa data.'}
                    return render(request,'encontro/cadastrarEncontro.html',data)
            except():
                data={'errorMessage': 'Valor de data inválido'}
                return render(request,'encontro/cadastrarEncontro.html',data)


        else:
            e = Encontro(dtEncontro=request.POST['dtEncontro'], nome=request.POST['temaEncontro'], registroPresenca='N')
            e.save()
            data = {'sucesso':'Encontro registrado com sucesso.'}
            return render(request, 'encontro/cadastrarEncontro.html', data)
    else:
        return render(request,'encontro/cadastrarEncontro.html')

def listaPresenca(request):

    turma = Turma.objects.get(ativo='S')
    crismando = Crismando.objects.filter(turma__anoTurma=turma.anoTurma)

    data = {'crismando': crismando}
    if request.POST:

        for cris_id in crismando:
            pres = request.POST['hide'+str(cris_id.id)]
            if pres == "presente":
                print("estou presente")
                presenca = Presenca(encontro=encontro,crismando=Crismando.objects.get(pk=cris_id.id))
                presenca.save()
        return redirect('crismando')
    else:
        return render(request,'crismando/registroPresenca.html', data)