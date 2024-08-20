from django.db import models

from core.models import Campeonato

class Time(models.Model):
    nome = models.CharField(max_length=100)
    gols_pro = models.IntegerField(blank=True, null=True)
    gols_contra = models.IntegerField(blank=True, null=True)
    vitoria = models.IntegerField(blank=True, null=True)
    derrota = models.IntegerField(blank=True, null=True)
    pontos = models.IntegerField(blank=True, null=True)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT, related_name="time", null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome} ({self.id})"
    