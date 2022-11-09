from django.shortcuts import render
from backend.serializers.evaluators import EvaluatorsSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.evaluators import Evaluator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class EvaluatorsModelViewSet(viewsets.ModelViewSet):
    queryset=Evaluator.objects.all()
    serializer_class=EvaluatorsSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['EvaluatorId','SId','UserId','PanelId']
    search_fields=['EvaluatorId','SId','UserId','name']
    odering_fields=['EvaluatorId']
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]