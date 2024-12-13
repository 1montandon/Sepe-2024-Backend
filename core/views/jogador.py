from core.models import Jogador
from core.serializers import JogadorDetailSerializer, JogadorWriteSerializer, JogadorCreateUpdateSerializer

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

@extend_schema(tags=["Jogador"])
class JogadorViewSet(ModelViewSet):
    queryset = Jogador.objects.order_by("-id")
    http_method_names = ["get", "post", "put", "patch", "delete"]
    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return JogadorCreateUpdateSerializer
        return JogadorDetailSerializer
    
    # @action(detail=False, methods=['get'])
    # def artilheiros(self, request):
    #     artilheiros = Jogador.objects.order_by("-gols")[:5]

    #     serializer = self.get_serializer(artilheiros, many=True)
    #     return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def artilheiros(self, request):
        jogadores = Jogador.objects.all()
        jogadores_with_gols = []

        for jogador in jogadores:
            # Use the logic from your serializer to calculate gols
            serializer = JogadorDetailSerializer(jogador)
            gols = serializer.get_gols(jogador)  # Call the method directly
            jogadores_with_gols.append({
                "jogador": jogador,
                "gols": len(gols),  # Assuming 'gols' is a list of goal objects
            })

        # Sort players by the number of goals in descending order
        sorted_jogadores = sorted(jogadores_with_gols, key=lambda x: x["gols"], reverse=True)

        # Get the top 5 players
        top_jogadores = sorted_jogadores[:5]

        # Serialize the top players
        data = [
            JogadorDetailSerializer(j["jogador"]).data for j in top_jogadores
        ]
        return Response(data)

