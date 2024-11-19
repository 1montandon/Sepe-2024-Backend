from rest_framework.serializers import ModelSerializer, CharField
from core.models import Jogo, Rodada
from core.serializers.time import TimeListSerializer

def update_create(instance):
    if instance.gols is None:
        # Inicialize `gols` como uma lista vazia ou retorne uma mensagem de erro, dependendo do caso de uso.
        instance.gols = []  # ou retorne um erro se necessário

        
    time_mandante = instance.time_mandante
    time_visitante = instance.time_visitante

    timeM_gols = 0
    timeV_gols = 0

    for gol in instance.gols:
        if gol is None:
                continue
        if gol["time"] is not None:
            print(time_mandante.id, "aqui viado")
            if gol["time"] == time_mandante.id:
                print(gol["time"])
                timeM_gols += 1
            elif gol["time"] != time_mandante.id:
                timeV_gols += 1

    if timeM_gols > timeV_gols:
        instance.vencedor = time_mandante
    elif timeM_gols < timeV_gols:
        instance.vencedor = time_visitante
    else:
        instance.vencedor = None

    instance.save()
    # return instance
class RodadaSerializer(ModelSerializer):
    class Meta:
        model = Rodada
        fields: list[str] = [
            "id",
            "numero_rodada",
        ]

class JogoDetailSerializer(ModelSerializer):
    time_visitante = TimeListSerializer()
    time_mandante = TimeListSerializer()
    rodada = RodadaSerializer()
    class Meta:
        model = Jogo
        fields: list[str] = [
            "id",
            "data",
            "horario",
            "endereco",
            "rodada",
            "time_mandante",
            "time_visitante",
            "gols",
            "cartoes",
            "vencedor",
            "tipo_jogo"
        ]

class JogoWriteSerializer(ModelSerializer):
    class Meta:
        model = Jogo
        fields: list[str] = [
            "id",
            "data",
            "horario",
            "endereco",
            "rodada",
            "time_mandante",
            "time_visitante",
            "gols",
            "cartoes",
            "tipo_jogo"

        ]
    def create(self, validated_data):
        # Create a new instance of Jogo with validated_data
        instance = Jogo(**validated_data)
        # ** - unpacks validated_data so that each key-value pair in the dictionary is treated as an individual argument, 
        # creating a Jogo instance with all the values in validated_data set as attributes on instance. 
        # This is particularly useful in Django or DRF, where model fields align with dictionary keys after validation, 
        # allowing you to easily create or update objects.
        print(Jogo(validated_data["data"]))
        print(Jogo(validated_data) )
        print(Jogo(**validated_data).data)
        print(Jogo(**validated_data))
        
        # Process the new instance using update_create
        update_create(instance)
        
        # Save and return the instance
        return instance

    def update(self, instance, validated_data):
        print(validated_data)
        instance.data = validated_data.get('data', instance.data)
        instance.horario = validated_data.get('horario', instance.horario)
        instance.endereco = validated_data.get('endereco', instance.endereco)
        instance.rodada = validated_data.get('rodada', instance.rodada)
        instance.time_mandante = validated_data.get('time_mandante', instance.time_mandante)
        instance.time_visitante = validated_data.get('time_visitante', instance.time_visitante)
        instance.gols = validated_data.get('gols', instance.gols)
        instance.cartoes = validated_data.get('cartoes', instance.cartoes)

        # for attr, value in validated_data.items():
        #     setattr(instance, attr, value)

        update_create(instance)
        return instance


