from django.db import models

class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.nome} ({self.id})"