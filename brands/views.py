from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Brand
from .serializers import BrandSerializer


class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
