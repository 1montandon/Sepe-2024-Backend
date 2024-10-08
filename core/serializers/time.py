from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Time, TimeJogador

class JogadorTimeSerializer(ModelSerializer):
    class Meta:
        model = TimeJogador
        fields = ('jogador',)
        depth = 2


class TimeDetailSerializer(ModelSerializer):
    escudo = ImageSerializer(required=False)
    jogadores = JogadorTimeSerializer(many=True)
    
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
            "campeonato", 
            "escudo", 
            "jogadores"
        ]


class TimeWriteSerializer(ModelSerializer):
    escudo_attachment_key = SlugRelatedField(
        source="escudo",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    escudo = ImageSerializer(required=False, read_only=True)
    
    class Meta:
        model = Time
        fields: list[str] = ["nome", "gols_pro", "gols_contra", "vitoria", "derrota", "pontos", "campeonato", "escudo_attachment_key", "escudo"]
