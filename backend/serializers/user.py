from rest_framework import serializers
from django.contrib.auth import get_user_model
from backend.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields="__all__"

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=["UserId","name","username"]
