from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, SerializerMethodField, IntegerField
from itertools import chain

from uploader.models import Image
from uploader.serializers import ImageSerializer, ImageListSerializer

from core.models import Time, TimeJogador, Jogo

class TimeJogadorSerializer(ModelSerializer):
    class Meta:
        model = TimeJogador
        fields = ("data_inicio", "jogador", "time")
        extra_kwargs = {
            "jogador": {"required": False},  # jogador is not required during validation
        }
        depth = 2

class TimeJogadorWriteSerializer(ModelSerializer):
    class Meta:
        model = TimeJogador
        fields = ("data_inicio", "jogador", "time")
        extra_kwargs = {
            "jogador": {"required": False},  # jogador is not required during validation
        }


class JogoSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = ('__all__')
        

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
    ultimos_jogos = SerializerMethodField()
    jogos = SerializerMethodField()

    def get_jogos(self, object):
        mandante = object.jogos_mandante.filter(jogo_realizado=True).order_by('-id')
        visitante = object.jogos_visitante.filter(jogo_realizado=True).order_by('-id')
        jogos = list(chain(mandante, visitante))
        serializer = JogoSerializer(jogos, many=True)
        return serializer.data

    

    def get_ultimos_jogos(self, object):
        mandante = object.jogos_mandante.filter(jogo_realizado=True).order_by('-id')[:5]
        visitante = object.jogos_visitante.filter(jogo_realizado=True).order_by('-id')[:5]
        jogos = list(chain(mandante, visitante))
        
        resultados = []
        for jogo in jogos:
            if jogo.vencedor == object:
                resultados.append(1)
            elif jogo.vencedor is None:
                resultados.append(0)
            else:
                resultados.append(-1)
        
        return resultados

        
        # print(object.id)
        # jogos = Jogo.objects.filter(Q(time_mandante__id=object.id | time_visitante__id=object.id))
        # return []


    jogadores = SerializerMethodField()

    def get_jogadores(self, object):
        jogadores = list()

        for time_jogador in object.jogadores.all():
            jogador = time_jogador.jogador
            if jogador.times.all()[len(jogador.times.all()) - 1].time.id == object.id:
                jogadores.append(time_jogador)

        return TimeJogadorSerializer(jogadores, many=True).data

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
            "ultimos_jogos",
            "jogos",
            "jogadores",
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
        fields: list[str] = ["nome",  "campeonato", "escudo_attachment_key", "escudo", "gols_pro", "gols_contra", "vitoria", "empate", "derrota", "pontos"]
