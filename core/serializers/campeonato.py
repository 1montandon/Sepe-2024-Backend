from rest_framework.serializers import ModelSerializer
from .core.models import Campeonato

class CampeonatoDetailSerializer(ModelSerializer):
    class Meta:
        model = System
        fields: list[str] = [
            "id",
            "name",
            "ano",
        ]
          

class CampeonatoWriteSerializer(ModelSerializer):
    class Meta:
        model = System
        fields: list[str] = [
            "name",
            "ano",
        ]
