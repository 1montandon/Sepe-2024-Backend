from django.db import models

class Time(models.Model):
    nome = models.CharField(max_length=100)
    gols_pro = models.IntegerField(blank=True, null=True)
    gols_contra = models.IntegerField(blank=True, null=True)
    vitoria = models.IntegerField(blank=True, null=True)
    derrota = models.IntegerField(blank=True, null=True)
    pontos = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nome} ({self.id})"
    