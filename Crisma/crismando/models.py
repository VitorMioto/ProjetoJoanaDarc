from django.db import models

# Create your models here.

class Turma(models.Model):
    anoTurma = models.IntegerField(primary_key=True)
    ativo = models.CharField(max_length=1)  # ativo = 1 não ativo = 0

    def __str__(self):
        return str(self.anoTurma)

    class Meta:
        verbose_name_plural = 'Turma'

class Crismando(models.Model):

    varSim = 'S'
    varNao = 'N'
    SIM_NAO_CHOICES = [(varSim,'Sim'), (varNao,'Não')]

    #sim = 1
    #nao = 0
    #comboSN = [(sim,'Sim'), (nao,'Não')]
    nome = models.CharField(max_length=100)
    dtNascimento = models.DateTimeField()
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    compl = models.CharField(max_length=15,null=True, blank=True)
    nomeMae = models.CharField(max_length=100)
    nomePai = models.CharField(max_length=100)
    telMae = models.CharField(max_length=15)
    telPai = models.CharField(max_length=15)
    fezBatismo = models.CharField(max_length=1,choices=SIM_NAO_CHOICES, default=varNao)
    fezComunhao = models.CharField(max_length=1,choices=SIM_NAO_CHOICES, default=varNao)
    turma = models.ForeignKey(Turma,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Crismando'


    def is_valid(self):
        if len(str(self.nome))==0:
            return 'Obrigatório preencher com o nome.',False
        elif len(str(self.dtNascimento))==0:
            return 'Obrigatório preencher a data de nascimento.',False
        elif len(str(self.endereco))==0:
            return 'Obrigatório preencher o endereço.', False
        elif len(str(self.numero))==0:
            return 'Obrigatório preencher o número.', False
        elif not str(self.numero).isdigit():
            return 'Apenas números no campo número.', False
        elif len(str(self.nomeMae))==0:
            return 'Obrigatório preencher com o nome da Mãe.', False
        elif len(str(self.nomePai))==0:
            return 'Obrigatório preencher com o nome do Pai.', False
        elif len(str(self.telMae))==0:
            return 'Obrigatório preencher com telefone da Mãe.', False
        elif len(str(self.telPai))==0:
            return 'Obrigatório preencher com o telefone do Pai.', False
        elif len(str(self.fezBatismo))==0:
            return 'Obrigatório selecionar se foi batizado.', False
        elif len(str(self.fezComunhao))==0:
            return 'Obrigatório selecionar se fez primeira comunhão.', False
        else:
            return '',True