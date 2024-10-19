from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Jogador, TimeJogador

class TimeJogadorSerializer(ModelSerializer):
    class Meta:
        model = TimeJogador
        fields = ('time',)
        depth = 2


class JogadorDetailSerializer(ModelSerializer):
    foto = ImageSerializer(required=False)
    times = TimeJogadorSerializer(many=True)

    class Meta:
        model = Jogador
        fields: list[str] = [
            "id",
            "nome",
            "idade",
            "email",
            "posicao",
            "numero",
            "foto",
            "times",
        ]


class JogadorWriteSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )

    class Meta:
        model = Jogador
        fields: list[str] = [
            "nome",
            "idade",
            "email",
            "posicao",
            "numero",
            "foto_attachment_key",
            "times",
        ]
