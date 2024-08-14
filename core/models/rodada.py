from django.db import models

class Rodada(models.Model):
    numero_rodada = models.IntegerField(null=False)
    data_inicio = models.DateField()
    data_termino = models.DateField()