from django.db import models

class Musica(models.Model):
    codMusica = models.IntegerField()
    nomeMusica = models.CharField(max_length=100)

class Repertorio(models.Model):
    dtMissa = models.DateField()
    #hrMissa (10h30, 19h, 9h,...)
    hrMissa = models.TimeField()
    #Tipo música (Entrada, Ato penitencial,...,Final)
    tipoMusica = models.CharField(max_length=20)
    musica = models.ForeignKey(Musica,on_delete=models.CASCADE)


