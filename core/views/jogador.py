from core.models import Jogador
from core.serializers import JogadorDetailSerializer, JogadorWriteSerializer, JogadorCreateUpdateSerializer

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@extend_schema(tags=["Jogador"])
class JogadorViewSet(ModelViewSet):
    queryset = Jogador.objects.order_by("-id")
    http_method_names = ["get", "post", "put", "patch", "delete"]
    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return JogadorCreateUpdateSerializer
        return JogadorCreateUpdateSerializer