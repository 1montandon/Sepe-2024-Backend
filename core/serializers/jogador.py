from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, SerializerMethodField, IntegerField

from uploader.models import Image
from uploader.serializers import ImageListSerializer

from core.models import Jogador, TimeJogador
from core.serializers.time import TimeJogadorSerializer

class JogadorCreateUpdateSerializer(ModelSerializer):
    times = TimeJogadorSerializer(many=True)
    class Meta:
        model = Jogador
        fields = ("nome", "idade", "email", "posicao", "numero", "times")

    def create(self, validated_data):
        print(validated_data)
        times_data = validated_data.pop("times")
        jogador = Jogador.objects.create(**validated_data)
        for time_data in times_data:
            TimeJogador.objects.create(jogador=jogador, **time_data)
        jogador.save()
        return jogador  
    
    def update(self, jogador, validated_data):
        times_data = validated_data.pop("times")
        if times_data:
            jogador.times.all().delete()
            for time_data in times_data:
                TimeJogador.objects.create(jogador=jogador, **time_data)
        return super().update(jogador, validated_data)

class JogadorDetailSerializer(ModelSerializer):
    foto = ImageListSerializer(required=False)
    times = TimeJogadorSerializer(many=True, read_only=True,)
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
            "times"
        ]


class JogadorWriteSerializer(ModelSerializer):
    times = TimeJogadorSerializer(many=True)
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
            "times"
        ]
