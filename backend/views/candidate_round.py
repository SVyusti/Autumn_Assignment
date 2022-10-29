from django.shortcuts import render
from backend.serializers.candidate_round import Candidate_roundSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.candidate_round import Candidate_round
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class Candidate_roundModelViewSet(viewsets.ModelViewSet):
    queryset=Candidate_round.objects.all()
    serializer_class=Candidate_roundSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['candidateId','RoundId']
    search_fields=['TimeSlot','candidateId','RoundStatus']
    odering_fields=['candidateId','RoundId','TimeSlot']
    odering=['RoundId']
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]