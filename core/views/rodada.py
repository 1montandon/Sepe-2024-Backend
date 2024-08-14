from core.models import Rodada
from core.serializers import RodadaDetailSerializer, RodadaWriteSerializer

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@extend_schema(tags=["Rodada"])
class RodadaViewSet(ModelViewSet):
    queryset = Rodada.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return RodadaDetailSerializer
        return RodadaWriteSerializer    