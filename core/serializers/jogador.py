from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, SerializerMethodField, IntegerField

from uploader.models import Image
from uploader.serializers import ImageListSerializer

from core.models import Jogador, TimeJogador

class TimeJogadorSerializer(ModelSerializer):
    id = IntegerField(source="time.id")
    nome = CharField(source="time.nome")
    gols_pro = IntegerField(source="time.gols_pro")
    gols_contra = IntegerField(source="time.gols_contra")
    vitoria = IntegerField(source="time.vitoria")
    empate = IntegerField(source="time.empate")
    derrota = IntegerField(source="time.derrota")
    pontos = IntegerField(source="time.pontos")
    campeonato = CharField(source="time.campeonato")
    escudo = CharField(source="time.escudo.url", required=False)

    class Meta:
        model = TimeJogador
        fields = (
            'id', 'nome', 'gols_pro', 'gols_contra', 'vitoria', 'empate',
            'derrota', 'pontos', 'campeonato', 'escudo',
        )


class JogadorDetailSerializer(ModelSerializer):
    foto = ImageListSerializer(required=False)
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
