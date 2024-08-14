from rest_framework.serializers import ModelSerializer
from core.models import Rodada

class RodadaDetailSerializer(ModelSerializer):
    class Meta:
        model = Rodada
        fields: list[str] = [
            "id",
            "numero_rodada",
            "data_inicio",
            "data_termino",
        ]
          

class RodadaWriteSerializer(ModelSerializer):
    class Meta:
        model = Rodada
        fields: list[str] = [
            "numero_rodada",
            "data_inicio",
            "data_termino",
        ]