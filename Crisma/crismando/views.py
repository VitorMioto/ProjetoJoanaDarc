from django.shortcuts import render, redirect
from .forms import CrismandoForm
from .models import Turma, Crismando
from encontro.models import Encontro, Presenca
from django.contrib.auth.decorators import login_required

# Create your views here.

def novoCrismando(request):
    turma = Turma.objects.get(ativo="S")
    data = {'turma': turma}
    if request.POST:
        crismando = Crismando(nome=request.POST['nome'], dtNascimento=request.POST['dtNasc'],
                              endereco=request.POST['endereco'], numero=request.POST['numero'],
                              compl=request.POST['compl'], nomeMae=request.POST['nomeMae'],
                              nomePai=request.POST['nomePai'], telMae=request.POST['telMae'],
                              telPai=request.POST['telPai'],fezBatismo=request.POST['fezBatismo'],
                              fezComunhao=request.POST['fezComunhao'], turma=Turma.objects.get(anoTurma=request.POST['turma']))
        errMessage, valid = crismando.is_valid()
        if valid:
            crismando.save()
        else:
            data['err']=errMessage
        return render(request, 'crismando/crismando.html', data)
    else:
        return render(request,'crismando/crismando.html',data)


#@login_required
def novaTurma(request):
    turma = Turma.objects.all().order_by('-anoTurma')
    data = {'turma':turma}
    if request.POST:

        if request.POST['ano']=='' or request.POST['ano']== None:
            data['errorMessage'] = 'Favor preencher o campo ano corretamente'
            return render(request, 'crismando/criarTurma.html', data)
        elif 'ativo' not in request.POST:
            data['errorMessage'] = 'Favor selecionar se está ativo ou não'
            return render(request, 'crismando/criarTurma.html', data)
        elif request.POST['ativo']=='' or request.POST['ativo']== None:
            data['errorMessage'] = 'Favor selecionar se está ativo ou não'
            return render(request, 'crismando/criarTurma.html', data)
        #elif tgAtiva not in ['S', 'N']:
        #    data['errorMessage'] = 'Não foi identificado tag válida para caixa de seleção.'
        #    return render(request, 'crismando/criarTurma.html', data)
        else:
            ano = request.POST['ano']
            ativo=request.POST['ativo']

            if ativo == 'S':
                for t in turma:
                    if t.ativo=='S' and t.anoTurma !=ano:
                        b = Turma.objects.get(anoTurma=t.anoTurma)
                        b.ativo = 'N'
                        b.save()
            b = Turma(anoTurma=ano, ativo=ativo)
            b.save()
            turma = Turma.objects.all().order_by('-anoTurma')
            data['sucesso'] = 'Registro salvo com sucesso'
            data['turma'] = turma
            return render(request,'crismando/criarTurma.html', data)
    else:
        return render(request,'crismando/criarTurma.html', data)


#@login_required
#antes de jogar para a lista de presença será necessário selecionar qual o dia do encontro, cada encontro deverá possuir uma lista de presença
#deve haver uma rota antes da lista de presença onde a pessoa irá selecionar de uma lista a data do encontro que irá preencher a lista de presença
#necessário criar outra rota para criar encontros, onde seja possível no futuro incluir uma lista de encontros (excel/json) ou uma opção de no próprio site montar uma lista e enviar por post no formato json?

#Criar app para encotrinho: funções, lista de confirmados...


#@login_required
#def listarTurma(request):
#    turma = Turma.objects.all()
#    data = {'turma':turma}
#    if request.POST:
#        pass
#    else:
#        return render(request,'crismando/listarTurma.html',data)

