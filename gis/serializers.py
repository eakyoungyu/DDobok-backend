from rest_framework import serializers
from .models import Gi


class GiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gi
        fields = "__all__"
