from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, SerializerMethodField
from itertools import chain

from uploader.models import Image
from uploader.serializers import ImageSerializer, ImageListSerializer

from core.models import Time, TimeJogador, Jogo

class JogadorTimeSerializer(ModelSerializer):
    class Meta:
        model = TimeJogador
        fields = ('jogador',)
        depth = 2

class TimeListSerializer(ModelSerializer):
    escudo = ImageListSerializer()
    class Meta:
        model = Time
        fields = [
            "nome",
            "id",
            "escudo"
        ]

class TimeDetailSerializer(ModelSerializer):
    escudo = ImageSerializer(required=False)
    jogadores = JogadorTimeSerializer(many=True)
    ultimos_jogos = SerializerMethodField()
    jogos = SerializerMethodField()

    def get_jogos(self, object):
        mandante = object.jogos_mandante.order_by('-id')
        visitante = object.jogos_visitante.order_by('-id')
        jogos = len(list(chain(mandante, visitante)))
        return jogos
    

    def get_ultimos_jogos(self, object):
        mandante = object.jogos_mandante.order_by('-id') if len(object.jogos_mandante.order_by('-id')) < 5 else object.jogos_mandante.order_by('-id')[:5]
        visitante = object.jogos_visitante.order_by('-id') if len(object.jogos_visitante.order_by('-id')) < 5 else object.jogos_visitante.order_by('-id')[:5]
        jogos = list(chain(mandante, visitante))
        resultados = []
        for jogo in jogos:
            if jogo.vencedor.id == object.id:
                resultados.append(1)
            elif jogo.vencedor == None:
                resultados.append(0)
            else:
                resultados.append({-1})
        return resultados
        
        # print(object.id)
        # jogos = Jogo.objects.filter(Q(time_mandante__id=object.id | time_visitante__id=object.id))
        # return []

    
    class Meta:
        model = Time
        fields: list[str] = [
            "id", 
            "nome", 
            "gols_pro", 
            "gols_contra", 
            "vitoria", 
            "empate",
            "derrota", 
            "pontos", 
            "campeonato", 
            "escudo", 
            "jogadores",
            "ultimos_jogos",
            "jogos"
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
        fields: list[str] = ["nome", "gols_pro", "gols_contra", "vitoria", "empate", "derrota", "pontos", "campeonato", "escudo_attachment_key", "escudo"]
