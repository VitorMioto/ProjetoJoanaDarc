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


@login_required
def novaTurma(request):
    turma = Turma.objects.all()
    data = {'turma':turma}
    if request.POST:
        ano = request.POST['ano']
        ativo = request.POST['ativo']
        #tgAtiva = request.POST['tgAtiva']

        if ano=='' or ano== None:
            data['errorMessage'] = 'Favor preencher o campo ano corretamente'
            return render(request, 'crismando/criarTurma.html', data)
        elif ativo=='' or ativo== None:
            data['errorMessage'] = 'Favor selecionar se está ativo ou não'
            return render(request, 'crismando/criarTurma.html', data)
        #elif tgAtiva not in ['S', 'N']:
        #    data['errorMessage'] = 'Não foi identificado tag válida para caixa de seleção.'
        #    return render(request, 'crismando/criarTurma.html', data)
        else:
            for t in turma:
                if t.anoTurma == int(ano) and t.ativo=='N' and ativo=='S':
                    b = Turma(anoTurma=int(ano),ativo='S')
                    b.save()
                    turma = Turma.objects.all()
                    data['sucesso'] = 'Registro atualizado com sucesso'
                    data['turma'] = turma
                    return render(request, 'crismando/criarTurma.html', data)
                elif t.anoTurma == int(ano) and t.ativo=='S' and ativo=='N':
                    b = Turma(anoTurma=int(ano), ativo='N')
                    b.save()
                    turma = Turma.objects.all()
                    data['sucesso'] = 'Registro atualizado com sucesso'
                    data['turma'] = turma
                    return render(request, 'crismando/criarTurma.html', data)




            for verfAtivo in turma:
                if verfAtivo.anoTurma == int(ano):
                    if ativo=='N':
                        data['errorMessage'] = 'Ano cadastrado anteriormente'
                        return render(request, 'crismando/criarTurma.html', data)
                    else:
                        b = Turma(anoTurma=ano, ativo='S')
                        b.save()
                if ativo == 'S':
                    for verfAtivo in turma:
                        if verfAtivo.ativo == 'S':
                            data['errorMessage'] = 'Já existe uma turma ativa: ' + str(verfAtivo.anoTurma)
                            return render(request, 'crismando/criarTurma.html', data)

            b = Turma(anoTurma=ano, ativo=ativo)
            b.save()
            turma = Turma.objects.all()
            data['sucesso'] = 'Registro salvo com sucesso'
            data['turma'] = turma
            return render(request,'crismando/criarTurma.html', data)
    else:
        return render(request,'crismando/criarTurma.html', data)


@login_required
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


#@login_required
#def listarTurma(request):
#    turma = Turma.objects.all()
#    data = {'turma':turma}
#    if request.POST:
#        pass
#    else:
#        return render(request,'crismando/listarTurma.html',data)

