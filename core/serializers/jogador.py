from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, SerializerMethodField, IntegerField

from uploader.models import Image
from uploader.serializers import ImageListSerializer

from core.models import Jogador, TimeJogador, Jogo
from core.serializers.time import TimeJogadorSerializer, TimeDetailSerializer, TimeListSerializer

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
    times = TimeJogadorSerializer(many=True, read_only=True)
    gols = SerializerMethodField()

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
            "gols",
        ]

    def get_gols(self, obj):
        jogos = Jogo.objects.all()  # Busca todos os jogos
        gols = []
        for jogo in jogos:
            # Confirme que 'gols' é uma lista válida
            jogo_gols = jogo.gols or []  # Define uma lista vazia se 'gols' for None

            # Filtra os gols que pertencem ao jogador
            # gols_do_jogador = [gol for gol in jogo_gols if gol.get("jogador") == obj.id] - [<expressão> for <variável> in <iterável> if <condição opcional>] 
            # Esse tipo de for é chamado de list comprehension em Python. É uma forma concisa e eficiente de criar listas com base em uma iteração.
            gols_do_jogador = []
            for gol in jogo_gols:
                if gol.get("jogador") == obj.id:
                    gols_do_jogador.append(gol)


            for gol in gols_do_jogador:
                gols.append({
                    "jogo": jogo.id,
                    "data": jogo.data.strftime("%d/%m/%Y"),
                    "time": gol["time"],
                    "time_visitante": TimeListSerializer(jogo.time_visitante).data ,
                    "time_mandante":  TimeListSerializer(jogo.time_mandante).data ,
                    "gol_pro": gol["gol_pro"],
                    "endereco": jogo.endereco,
                    "tipo_jogo": jogo.tipo_jogo,
                })

        return gols


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
