from rest_framework import serializers
from backend.models import user 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user.User
        fields="__all__"
