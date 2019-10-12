from django.db import models

# Create your models here.
class Alcada(models.Model):
    alcadaNome = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Alcada'

    def __str__(self):
        return self.alcadaNome

class Usuario(models.Model):
    userID = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    alcada = models.ForeignKey(Alcada, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Usuario'

    def __str__(self):
        return self.userID