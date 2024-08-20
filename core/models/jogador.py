from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import Time

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=150)
    posicao = models.CharField(max_length=50, null=True)
    numero = models.PositiveIntegerField(
        blank=True, 
        null=True,         
        default=0,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(1)
        ]
    )
    time = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="jogador", blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.id})"
