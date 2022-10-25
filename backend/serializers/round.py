from rest_framework import serializers
from backend.models import round 
from backend.serializers.season import SeasonSerializer

class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model=round.Round
        fields="__all__"
