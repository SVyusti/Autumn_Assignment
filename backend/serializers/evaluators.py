from rest_framework import serializers
from backend.models import evaluators 

class EvaluatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=evaluators.Evaluator
        fields="__all__"
