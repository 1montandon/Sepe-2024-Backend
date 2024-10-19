from rest_framework.serializers import ModelSerializer
from core.models import TimeJogador


class TimeJogadorDetailSerializer(ModelSerializer):
    class Meta:
        model = TimeJogador
        fields: list[str] = [
            "id",
            "data_inicio",
            "data_termino",
            "jogador",
            "time",
        ]
        depth = 2

class TimeJogadorWriteSerializer(ModelSerializer):
    class Meta:
        model = TimeJogador
        fields: list[str] = [
            "data_inicio",
            "data_termino",
            "jogador",
            "time",
        ]