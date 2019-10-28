from django.db import models
from crismando.models import Crismando, Turma
# Create your models here.

class Encontro(models.Model):
    dtEncontro = models.DateField()
    nome = models.CharField(max_length=100)
    registroPresenca = models.CharField(max_length=1)
    #turma =  models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Encontro'

class Presenca(models.Model):
    encontro = models.ForeignKey(Encontro, on_delete=models.CASCADE)
    crismando = models.ForeignKey(Crismando, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.encontro)

    class Meta:
        verbose_name_plural = 'Presenca'