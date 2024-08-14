from core.models import Campeonato
from core.serializers import CampeonatoDetailSerializer, CampeonatoWriteSerializer

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@extend_schema(tags=["Campeonato"])
class CampeonatoViewSet(ModelViewSet):
    queryset = Campeonato.objects.all()
    # http_method_names = ["get", "post", "put", "delete"]
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CampeonatoDetailSerializer
        return CampeonatoWriteSerializer    