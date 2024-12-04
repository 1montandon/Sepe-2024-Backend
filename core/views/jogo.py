from core.models import Jogo, Time, Rodada, Campeonato
from core.serializers import JogoDetailSerializer, JogoWriteSerializer

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@extend_schema(tags=["Jogo"])
class JogoViewSet(ModelViewSet):
    queryset = Jogo.objects.all()
    http_method_names = ["get", "post", "put", "delete", "patch"]
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return JogoDetailSerializer
        return JogoWriteSerializer    

    @action(detail=False, methods=['post'])
    def gerar_semifinais(self, pk=None):
        campeonato = Campeonato.objects.order_by('-id').first()
        rodada = Rodada.objects.create(numero_rodada=len(Rodada.objects.all()) + 1, campeonato=campeonato)
        times_ordenados = Time.objects.order_by('-pontos')
        Jogo.objects.create(time_mandante=times_ordenados[0], time_visitante=times_ordenados[3], rodada=rodada, tipo_jogo=Jogo.opcoes_de_jogos.SEMI, data='2022-12-12', horario='12:00')
        Jogo.objects.create(time_mandante=times_ordenados[1], time_visitante=times_ordenados[2], rodada=rodada, tipo_jogo=Jogo.opcoes_de_jogos.SEMI, data='2022-12-12', horario='12:00')
        
        return Response(status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def gerar_finais(self, pk=None):
        campeonato = Campeonato.objects.order_by('-id').first()
        rodada = Rodada.objects.create(numero_rodada=len(Rodada.objects.all()) + 1, campeonato=campeonato)
        
        vencedores = []
        for jogo in Jogo.objects.filter(tipo_jogo=Jogo.opcoes_de_jogos.SEMI):
                vencedores.append(jogo.vencedor)    

        print(vencedores)


        Jogo.objects.create(time_mandante=vencedores[0], time_visitante=vencedores[1], rodada=rodada, tipo_jogo=Jogo.opcoes_de_jogos.FINAL, data='2022-12-12', horario='12:00')
        
        return Response(status=status.HTTP_201_CREATED)