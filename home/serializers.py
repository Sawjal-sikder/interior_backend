from rest_framework import serializers
from .models import Banar


class BanarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banar
        fields = '__all__'
