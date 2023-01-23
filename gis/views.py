from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Gi
from .serializers import GiSerializer


class GiViewSet(ModelViewSet):
    serializer_class = GiSerializer
    queryset = Gi.objects.all()
