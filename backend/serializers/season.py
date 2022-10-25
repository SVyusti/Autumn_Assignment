from rest_framework import serializers
from backend.models import season

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model=season.Season
        fields="__all__"