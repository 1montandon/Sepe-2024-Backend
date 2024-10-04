from django.db import models

from core.models import Rodada, Time

class Jogo(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    endereco = models.CharField(max_length=150)
    rodada = models.ForeignKey(Rodada, on_delete=models.PROTECT, related_name="jogos")
    time_mandante = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="jogos_mandante")
    time_visitante = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="jogos_visitante")
    time_mandante_escudo = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="time_mandante")
    time_visitante_escudo = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="time_visitante")
    gols = models.JSONField(null=True, blank=True)
    cartoes = models.JSONField(null=True, blank=True)

    