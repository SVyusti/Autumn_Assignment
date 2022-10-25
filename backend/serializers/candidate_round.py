from rest_framework import serializers
from backend.models import candidate_round 

class Candidate_roundSerializer(serializers.ModelSerializer):
    class Meta:
        model=candidate_round.Candidate_round
        fields="__all__"
