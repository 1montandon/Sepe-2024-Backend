from core.models import Jogo
from core.serializers import JogoDetailSerializer, JogoWriteSerializer

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