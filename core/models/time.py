from django.db import models
from uploader.models import Image
from core.models import Campeonato


class Time(models.Model):
    nome = models.CharField(max_length=100)
    gols_pro = models.IntegerField(blank=True, null=True, default=0)
    gols_contra = models.IntegerField(blank=True, null=True, default=0)
    vitoria = models.IntegerField(blank=True, null=True, default=0)
    derrota = models.IntegerField(blank=True, null=True, default=0)
    pontos = models.IntegerField(blank=True, null=True, default=0)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT, related_name="time", null=True, blank=True)
    escudo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    
    def __str__(self):
        return f"{self.nome} ({self.id})"
    