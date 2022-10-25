from rest_framework import serializers
from backend.models import candidates 

class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=candidates.Candidates
        fields="__all__"
