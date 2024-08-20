from django.db import models

from core.models import Campeonato

class Rodada(models.Model):
    numero_rodada = models.IntegerField(null=False)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT, related_name="rodada", null=True, blank=True)