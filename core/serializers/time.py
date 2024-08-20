from rest_framework.serializers import ModelSerializer
from core.models import Time

class TimeDetailSerializer(ModelSerializer):
    class Meta:
        model = Time
        fields: list[str] = [
            "id",
            "nome",
            "gols_pro",
            "gols_contra",
            "vitoria",
            "derrota",
            "pontos",
            "campeonato"
        ]
          

class TimeWriteSerializer(ModelSerializer):
    class Meta:
        model = Time
        fields: list[str] = [
            "nome",
            "gols_pro",
            "gols_contra",
            "vitoria",
            "derrota",
            "pontos",
            "campeonato"
        ]
