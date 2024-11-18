from rest_framework.serializers import ModelSerializer
from core.models import Rodada
from core.serializers.jogo import JogoDetailSerializer

class RodadaDetailSerializer(ModelSerializer):
    jogos = JogoDetailSerializer(many=True)
    class Meta:
        model = Rodada
        fields: list[str] = [
            "id",
            "numero_rodada",
            "campeonato",
            "jogos"
        ]
          

class RodadaWriteSerializer(ModelSerializer):
    class Meta:
        model = Rodada
        fields: list[str] = [
            "numero_rodada",
            "campeonato"
        ]