from rest_framework.serializers import ModelSerializer
from core.models import Jogo

class JogoDetailSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields: list[str] = [
            "id",
            "data",
            "horario",
            "endereco",
            "rodada",
            "time_mandante",
            "time_visitante",
            "gols",
            "cartoes"           
]

class JogoWriteSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields: list[str] = [
            "data",
            "horario",
            "endereco",
            "rodada",
            "time_mandante",
            "time_visitante",
            "gols",
            "cartoes"           
]