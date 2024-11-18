from django.db import models

from core.models import Campeonato

class Rodada(models.Model):
    numero_rodada = models.IntegerField(null=False)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT, related_name="rodada", null=True, blank=True)