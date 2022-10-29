from rest_framework import serializers
from backend.models import candidates
from backend.serializers.round import RoundSerializer
from backend.serializers.season import SeasonSerializer 

class CandidatesfoSerializer(serializers.ModelSerializer):
    rounds=RoundSerializer(many=True)
    season=SeasonSerializer()
    class Meta:
        model=candidates.Candidates
        fields="__all__"

class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=candidates.Candidates
        fields="__all__"

class CandidatesContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=candidates.Candidates
        fields=['StudentId','name','phone']
