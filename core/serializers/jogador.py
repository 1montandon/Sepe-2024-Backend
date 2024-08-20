from rest_framework.serializers import ModelSerializer
from core.models import Jogador


class JogadorDetailSerializer(ModelSerializer):
    class Meta:
        model = Jogador
        fields: list[str] = [
            "id",
            "nome",
            "idade",
            "email",
            "posicao",
            "numero",
            "time"
        ]


class JogadorWriteSerializer(ModelSerializer):
    class Meta:
        model = Jogador
        fields: list[str] = [
            "nome",
            "idade",
            "email",
            "posicao",
            "numero",
            "time"
        ]
