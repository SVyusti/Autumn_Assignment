from django.shortcuts import render
from .serializers import *
# Create your views here.
from rest_framework import viewsets
from .models import *
class SeasonModelViewSet(viewsets.ModelViewSet):
    queryset=Season.objects.all()
    serializer_class=SeasonSerializer