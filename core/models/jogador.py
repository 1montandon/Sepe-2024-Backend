from django.db import models


class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(max_digits=3, blank=True, null=True)
    email = models.EmailField(max_length=150)
    posicao = models.CharField(max_length=50, null=True)
    numero = models.IntegerField(max_digits=2, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.id})"
