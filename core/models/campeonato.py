from django.db import models

class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField(null=False)
    mata_mata = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} ({self.id}) {self.mata_mata}"