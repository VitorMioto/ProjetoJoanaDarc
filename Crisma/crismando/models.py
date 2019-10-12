from django.db import models

# Create your models here.

class Turma(models.Model):
    anoTurma = models.IntegerField()
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
    numero = models.CharField(max_length=5)
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


