from django.shortcuts import render
from backend.serializers.round import RoundSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.round import Round
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class RoundModelViewSet(viewsets.ModelViewSet):
    queryset=Round.objects.all()
    serializer_class=RoundSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['S_Id','type','role']
    search_fields=['S_Id','type','role']
    odering_fields=['S_Id']
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]