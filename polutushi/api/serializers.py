from rest_framework import serializers
from polutushi.models import Polutushi

class PolutushiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polutushi
        fields = ['id', 'weight', 'image']