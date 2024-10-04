from rest_framework.serializers import ModelSerializer, CharField
from core.models import Jogo

class JogoDetailSerializer(ModelSerializer):
    time_mandante = CharField(source='time_mandante.nome')
    time_visitante = CharField(source='time_visitante.nome')
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