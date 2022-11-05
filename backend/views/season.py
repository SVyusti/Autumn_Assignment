from django.shortcuts import render
from backend.serializers.season import SeasonSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.season import Season
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
# from backend.custompermissions import CustomAuthentication

class SeasonModelViewSet(viewsets.ModelViewSet):
    queryset=Season.objects.all()
    serializer_class=SeasonSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['Id','year']
    search_fields=['year']
    odering_fields=['Id','year']
    # authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]