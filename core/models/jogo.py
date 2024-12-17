from django.db import models

from core.models import Rodada, Time, Campeonato
from django.db.models.signals import post_save
from django.dispatch import receiver


class Jogo(models.Model):
    data = models.DateField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    rodada = models.ForeignKey(Rodada, on_delete=models.PROTECT, related_name="jogos", blank=True, null=True)
    time_mandante = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="jogos_mandante", null=True, blank=True)
    time_visitante = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="jogos_visitante", null=True, blank=True)
    gols = models.JSONField(null=True, blank=True)
    vencedor = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="+", blank=True, null=True)
    cartoes = models.JSONField(null=True, blank=True)
    class opcoes_de_jogos(models.TextChoices):
        GRUPOS = "Grupo",("Grupo")
        SEMI = "Semi", ("Semi")
        FINAL = "Final",("Final")

    tipo_jogo = models.CharField( max_length=5, choices=opcoes_de_jogos, default=opcoes_de_jogos.GRUPOS)
    jogo_realizado = models.BooleanField(default=False)


@receiver(post_save, sender=Jogo)
def vitoria_derrota(sender, instance, **kwargs):
    time_mandante = instance.time_mandante
    time_visitante = instance.time_visitante

    time_mandante.vitoria = 0
    time_mandante.empate = 0
    time_mandante.derrota = 0
    time_mandante.pontos = 0 
    time_visitante.vitoria = 0
    time_visitante.empate = 0
    time_visitante.derrota = 0
    time_visitante.pontos = 0 
    timeM_gols = 0
    timeV_gols = 0 

    time_mandante.save()
    time_visitante.save()
    
    jogos_mandante = list(time_mandante.jogos_mandante.all()) + list(time_mandante.jogos_visitante.all())
    jogos_visitante = list(time_visitante.jogos_mandante.all()) + list(time_visitante.jogos_visitante.all())

    # print(list(jogos_mandante + jogos_visitante))
    campeonato = instance.rodada.campeonato

        
    for jogo in jogos_mandante:
        if jogo.jogo_realizado is True and jogo.tipo_jogo == Jogo.opcoes_de_jogos.GRUPOS:
            if jogo.gols:
                for gol in jogo.gols:
                        if gol is None:
                            continue
                        if gol["time"] is not None:
                            if gol["time"] == time_mandante.id:
                                timeM_gols += 1
                            elif gol["time"] is not time_mandante.id:
                                timeV_gols += 1
                                
                if timeM_gols > timeV_gols:
                            time_mandante.vitoria += 1
                            time_mandante.pontos += 3
                            timeM_gols = 0
                            timeV_gols = 0
                            time_mandante.save()
                elif timeV_gols > timeM_gols:
                            time_mandante.derrota += 1
                            timeM_gols = 0
                            timeV_gols = 0
                            time_mandante.save()
                else:
                            time_mandante.empate += 1
                            time_mandante.pontos += 1
                            timeM_gols = 0
                            timeV_gols = 0
                            time_mandante.save()
            else:
                time_mandante.empate += 1
                time_mandante.pontos += 1
                timeM_gols = 0
                timeV_gols = 0
                time_mandante.save()
        else:
            None


    for jogo in jogos_visitante:
        if jogo.jogo_realizado is True and jogo.tipo_jogo == Jogo.opcoes_de_jogos.GRUPOS:
            if jogo.gols:
                for gol in jogo.gols:
                        if gol is None:
                            continue
                        if gol["time"] is not None:
                            if gol["time"] == time_visitante.id:
                                timeV_gols += 1
                            elif gol["time"] is not time_visitante.id:
                                timeM_gols += 1
                                
                if timeV_gols > timeM_gols:
                            time_visitante.vitoria += 1
                            time_visitante.pontos += 3
                            timeM_gols = 0
                            timeV_gols = 0
                            time_visitante.save()
                elif timeM_gols > timeV_gols:
                            time_visitante.derrota += 1
                            timeM_gols = 0
                            timeV_gols = 0
                            time_visitante.save()
                else:
                            time_visitante.empate += 1
                            time_visitante.pontos += 1
                            timeM_gols = 0
                            timeV_gols = 0
                            time_visitante.save()   
            else:
                time_visitante.empate += 1
                time_visitante.pontos += 1
                timeM_gols = 0
                timeV_gols = 0
                time_visitante.save()   
        else:
            None
  


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

    campeonato = instance.rodada.campeonato


    for jogo in jogos_mandante:
        if jogo.jogo_realizado is True and jogo.tipo_jogo == Jogo.opcoes_de_jogos.GRUPOS:
            if jogo.gols is None:
                continue
            for gol in jogo.gols:
                if gol is None:
                    continue
                if gol["time"] is not None:
                    if gol["time"] == time_mandante.id:
                        time_mandante.gols_pro += 1
                        time_mandante.save()
                    else:
                        time_mandante.gols_contra += 1
                        time_mandante.save()
                else:
                    continue
                

    for jogo in jogos_visitante:
        if jogo.jogo_realizado is True and jogo.tipo_jogo == Jogo.opcoes_de_jogos.GRUPOS:
            if jogo.gols is None:
                continue
            for gol in jogo.gols:
                if gol is None:
                    continue
                if gol["time"] is not None:
                    if gol["time"] == time_visitante.id:
                        time_visitante.gols_pro += 1
                        time_visitante.save()
                    else:
                        time_visitante.gols_contra += 1
                        time_visitante.save()
                else:
                    continue

