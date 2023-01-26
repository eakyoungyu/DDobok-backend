from django.shortcuts import render
from django_filters import FilterSet, NumberFilter, MultipleChoiceFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from .models import Gi
from .serializers import GiSerializer


class GiFilterSet(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr="gte")
    max_price = NumberFilter(field_name="price", lookup_expr="lte")
    color = MultipleChoiceFilter(choices=Gi.Color.choices)

    class Meta:
        model = Gi
        fields = ("price", "color", "priority")


class GiViewSet(ModelViewSet):
    serializer_class = GiSerializer
    queryset = Gi.objects.all()
    filterset_class = GiFilterSet
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering = ("-priority",)
