from django.db import models

from core.models import Rodada, Time
from django.db.models.signals import post_save
from django.dispatch import receiver


class Jogo(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    endereco = models.CharField(max_length=150)
    rodada = models.ForeignKey(Rodada, on_delete=models.PROTECT, related_name="jogos")
    time_mandante = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="jogos_mandante")
    time_visitante = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="jogos_visitante")
    gols = models.JSONField(null=True, blank=True)
    vencedor = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="+", blank=True, null=True)
    cartoes = models.JSONField(null=True, blank=True)


@receiver(post_save, sender=Jogo)
def vitoria_derrota(sender, instance, **kwargs):
    time_mandante = instance.time_mandante
    time_visitante = instance.time_visitante

    timeM_gols = 0
    timeV_gols = 0 

   
    for gol in instance.gols:
            if gol is None:
                continue
            if gol["time"] is not None:
                if gol["time"] == time_mandante.id:
                    timeM_gols += 1
                elif gol["time"] is not time_mandante.id:
                    timeV_gols += 1
                    
    if timeM_gols > timeV_gols:
                time_mandante.vitoria += 1
                time_visitante.derrota += 1
                time_mandante.pontos += 3
                timeM_gols = 0
                timeV_gols = 0
                time_mandante.save()
                time_visitante.save()
    elif timeM_gols < timeV_gols:
                time_visitante.vitoria += 1
                time_mandante.derrota += 1
                time_visitante.pontos += 3
                timeM_gols = 0
                timeV_gols = 0
                time_mandante.save()
                time_visitante.save()
    else:
                time_mandante.empate += 1
                time_visitante.empate += 1
                time_mandante.pontos += 1
                time_visitante.pontos += 1
                timeM_gols = 0
                timeV_gols = 0
                time_mandante.save()
                time_visitante.save()
                


@receiver(post_save, sender=Jogo)
def update_gols(sender, instance, **kwargs):
    time_mandante = instance.time_mandante
    time_visitante = instance.time_visitante

    time_mandante.gols_pro = 0
    time_visitante.gols_pro = 0
    time_visitante.gols_contra = 0
    time_mandante.gols_contra = 0

    time_mandante.save()
    time_visitante.save()

    jogos_mandante = list(time_mandante.jogos_mandante.all()) + list(time_mandante.jogos_visitante.all())
    jogos_visitante = list(time_visitante.jogos_mandante.all()) + list(time_visitante.jogos_visitante.all())

    for jogo in jogos_mandante:
        if jogo.gols is None:
            continue
        for gol in jogo.gols:
            if gol is None:
                continue
            if gol["time"] is not None:
                if gol["time"] == time_mandante.id:
                    time_mandante.gols_pro += 1
                    time_mandante.save()
                elif gol["time"] is not time_mandante.id:
                    time_mandante.gols_contra += 1
                    time_mandante.save()
            else:
                continue

    for jogo in jogos_visitante:
        if jogo.gols is None:
            continue
        for gol in jogo.gols:
            if gol is None:
                continue
            if gol["time"] is not None:
                if gol["time"] == time_visitante.id:
                    time_visitante.gols_pro += 1
                    time_visitante.save()
                elif gol["time"] is not time_visitante.id:
                    time_visitante.gols_contra += 1
                    time_visitante.save()
            else:
                continue