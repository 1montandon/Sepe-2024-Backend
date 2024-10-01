from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from uploader.models import Image



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
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    # time_jogador = models.ForeignKey("TimeJogador", on_delete=models.PROTECT, related_name="time_jogador", null=True, blank=True)
    class PosicaoJogador(models.IntegerChoices):
        GOLEIRO = 1, "Goleiro"
        FIXO = 2, "Fixo"
        ALA = 3, "Ala"
        PIVO = 4, "Pivo"

    posicao = models.IntegerField(choices=PosicaoJogador.choices)

    def __str__(self):
        return f"{self.nome} ({self.id})"
