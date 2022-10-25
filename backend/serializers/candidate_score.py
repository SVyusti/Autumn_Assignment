from rest_framework import serializers
from backend.models import candidate_score 

class Candidate_scoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=candidate_score.Candidate_score
        fields="__all__"
