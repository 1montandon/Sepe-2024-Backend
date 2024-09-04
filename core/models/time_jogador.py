from django.db import models 

from core.models import Jogador, Time

class TimeJogador(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField()
    jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT, related_name="jogador")
    time = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="time")