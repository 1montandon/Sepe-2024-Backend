from rest_framework.serializers import ModelSerializer
from core.models import Campeonato

class CampeonatoDetailSerializer(ModelSerializer):
    class Meta:
        model = Campeonato
        fields: list[str] = [
            "id",
            "nome",
            "ano",
            "mata_mata",
        ]
          

class CampeonatoWriteSerializer(ModelSerializer):
    class Meta:
        model = Campeonato
        fields: list[str] = [
            "nome",
            "ano",
            "mata_mata",
        ]
