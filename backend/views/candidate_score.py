from django.shortcuts import render
from backend.serializers.candidate_score import Candidate_scoreSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.candidate_score import Candidate_score
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class Candidate_scoreModelViewSet(viewsets.ModelViewSet):
    queryset=Candidate_score.objects.all()
    serializer_class=Candidate_scoreSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['studentId','QuestionId']
    search_fields=['studentId','QuestionId']
    odering_fields=['studentId','QuestionId']
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]