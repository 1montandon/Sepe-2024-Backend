from core.models import Time, Jogador
from core.serializers import TimeDetailSerializer, TimeWriteSerializer
from django.db.models import Max, F

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@extend_schema(tags=["Time"])
class TimeViewSet(ModelViewSet):
    queryset = Time.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TimeDetailSerializer
        return TimeWriteSerializer
