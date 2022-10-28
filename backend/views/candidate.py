from django.shortcuts import render
from backend.serializers.candidates import CandidatesSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.candidates import Candidates
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class SeasonModelViewSet(viewsets.ModelViewSet):
    queryset=Candidates.objects.all()
    serializer_class=CandidatesSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['name','EnrollmentNo']
    search_fields=['name','EnrollmentNo']
    odering_fields=['name','EnrollmentNo']
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]