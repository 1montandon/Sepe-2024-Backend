from core.models import TimeJogador
from core.serializers import TimeJogadorDetailSerializer, TimeJogadorWriteSerializer

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@extend_schema(tags=["TimeJogador"])
class TimeJogadorViewSet(ModelViewSet):
    queryset = TimeJogador.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TimeJogadorDetailSerializer
        return TimeJogadorWriteSerializer 