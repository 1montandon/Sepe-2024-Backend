from rest_framework.serializers import ModelSerializer, CharField
from core.models import Jogo
from core.serializers.time import TimeListSerializer

def update_create(instance):
    time_mandante = instance.time_mandante
    time_visitante = instance.time_visitante

    timeM_gols = 0
    timeV_gols = 0

    for gol in instance.gols:
        if gol is None:
                continue
        if gol["time"] is not None:
            if gol["time"] == time_mandante.id:
                timeM_gols += 1
            elif gol["time"] is not time_mandante.id:
                timeV_gols += 1

    if timeM_gols > timeV_gols:
        instance.vencedor = time_mandante
    elif timeM_gols < timeV_gols:
        instance.vencedor = time_visitante
    else:
        instance.vencedor = None

class JogoDetailSerializer(ModelSerializer):
    # time_mandante = CharField(source='time_mandante.nome')
    # time_visitante = CharField(source='time_visitante.nome')
    time_visitante = TimeListSerializer()
    time_mandante = TimeListSerializer()

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
            "cartoes",
            "vencedor"
        ]

class JogoWriteSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields: list[str] = [
            "data",''
            "horario",
            "endereco",
            "rodada",
            "time_mandante",
            "time_visitante",
            "gols",
            "cartoes",
        ]
    def create(self, validated_data):
        update_create()
        return 

    def update(self, instance, validated_data):
        update_create(instance)

        instance.save()
        return instance


