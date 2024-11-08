from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, SerializerMethodField, IntegerField
from itertools import chain

from uploader.models import Image
from uploader.serializers import ImageSerializer, ImageListSerializer

from core.models import Time, TimeJogador, Jogo

class JogoSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields = ('__all__')
        
class JogadorTimeSerializer(ModelSerializer):
    id = IntegerField(source="jogador.id")
    nome = CharField(source="jogador.nome")
    idade = IntegerField(source="jogador.idade")
    email = CharField(source="jogador.email")
    numero = IntegerField(source="jogador.numero")
    posicao = IntegerField(source="jogador.posicao")
    foto = CharField(source="jogador.foto.url", required=False)
    class Meta:
        model = TimeJogador
        fields = ('id', 'nome', 'idade', 'email', 'numero', 'posicao', 'foto')

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
        jogos = list(chain(mandante, visitante)) #Antes era so usado para pegar o length do jogos
        # Use JogoSerializer to serialize each Jogo instance
        serializer = JogoSerializer(jogos, many=True)
        print("AQUI BURRO",serializer, serializer.data)
        return serializer.data
    

    def get_ultimos_jogos(self, object):
        mandante = object.jogos_mandante.order_by('-id') if len(object.jogos_mandante.order_by('-id')) < 5 else object.jogos_mandante.order_by('-id')[:5]
        visitante = object.jogos_visitante.order_by('-id') if len(object.jogos_visitante.order_by('-id')) < 5 else object.jogos_visitante.order_by('-id')[:5]
        jogos = list(chain(mandante, visitante))
        resultados = []
        for jogo in jogos:
            print(jogo.vencedor, object)
            if jogo.vencedor == object:
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
