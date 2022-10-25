
from rest_framework import serializers
from backend.models import section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=section.Section
        fields="__all__"
