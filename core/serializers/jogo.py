from rest_framework.serializers import ModelSerializer, CharField
from core.models import Jogo
from core.serializers.time import TimeListSerializer

class JogoDetailSerializer(ModelSerializer):
    # time_mandante = CharField(source='time_mandante.nome')
    # time_visitante = CharField(source='time_visitante.nome')
    time_visitante = TimeListSerializer()
    time_mandante = TimeListSerializer()
    time_mandante_escudo = CharField(source='time_mandante.escudo.url')
    time_visitante_escudo = CharField(source='time_visitante.escudo.url')
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
            "time_mandante_escudo",
            "time_visitante_escudo",
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