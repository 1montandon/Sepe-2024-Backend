from django.db import models
from uploader.models import Image
from core.models import Campeonato
from core.models.jogador import Jogador


class Time(models.Model):
    nome = models.CharField(max_length=100)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT, related_name="time", null=True, blank=True)
    escudo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default="https://i.ibb.co/VDwW5Rv/28-289657-espn-soccer-team-logo-default.png",
    )
    gols_pro = models.IntegerField(blank=True, null=True, default=0)
    gols_contra = models.IntegerField(blank=True, null=True, default=0)
    vitoria = models.IntegerField(blank=True, null=True, default=0)
    empate = models.IntegerField(blank=True, null=True, default=0)
    derrota = models.IntegerField(blank=True, null=True, default=0)
    pontos = models.IntegerField(blank=True, null=True, default=0)
    
    def __str__(self):
        return f"{self.nome} ({self.id})"

class TimeJogador(models.Model):
    data_inicio = models.DateField(auto_now_add=True)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name="times")
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name="jogadores")