from rest_framework import serializers
from backend.models import question 

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=question.Question
        fields="__all__"
