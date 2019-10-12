from django.shortcuts import render, redirect
from .forms import CrismandoForm
from .models import Turma, Crismando
from encontro.models import Encontro, Presenca

# Create your views here.

def novoCrismando(request):
    form = CrismandoForm(request.POST or None)
    data = {'form': form}
    if form.is_valid():
        form.save()
        #return redirect(request, 'home.html')

    return render(request,'crismando/crismando.html',data)

def novaTurma(request):
    turma = Turma.objects.all()
    if request.POST:
        ano = request.POST['ano']
        ativo = request.POST['ativo']
        if ano=='' or ano== None:
            return render(request, 'crismando/turmaAtiva.html', {'errorMessage': 'Favor preencher o campo ano corretamente'})
        elif ativo=='' or ativo== None:
            return render(request, 'crismando/turmaAtiva.html', {'errorMessage': 'Favor selecionar se está ativo ou não'})
        else:
            for verfativo in turma:
                if verfativo.anoTurma == int(ano):
                    return render(request, 'crismando/turmaAtiva.html',
                                  {'errorMessage': 'Já existe esse ano cadastrado'})
            if ativo == 'S':
                for verfativo in turma:
                    if verfativo.ativo == 'S':
                        return render(request, 'crismando/turmaAtiva.html',
                                      {'errorMessage':'Já existe uma turma ativa: ' + str(verfativo.anoTurma)})
            b = Turma(anoTurma=ano, ativo=ativo)
            b.save()
            sucesso = 'Registro salvo com sucesso'
            return redirect('crismando')
    else:
        return render(request,'crismando/turmaAtiva.html')

def listaPresenca(request):

    turma = Turma.objects.get(ativo='S')
    crismando = Crismando.objects.filter(turma__anoTurma=turma.anoTurma)
    data = {'crismando': crismando}
    if request.POST:
        dtEncontro = request.POST['dtEncontro']
        print(dtEncontro)
        nomeEncontro = request.POST['temaEncontro']

        if len(Encontro.objects.filter(dtEncontro=dtEncontro))==0:
            encontro = Encontro(dtEncontro = dtEncontro, nome = nomeEncontro, turma= turma)
            encontro.save()
        else:
            data['erroDt'] = 'Já foi registrado um encontro nesta data'
            return render(request, 'crismando/registroPresenca.html', data)
            #Erro: Já existe essa data de encontro

        for cris_id in crismando:
            pres = request.POST['hide'+str(cris_id.id)]
            if pres == "presente":
                print("estou presente")
                presenca = Presenca(encontro=encontro,crismando=Crismando.objects.get(pk=cris_id.id))
                presenca.save()
        return redirect('crismando')
    else:
        return render(request,'crismando/registroPresenca.html', data)