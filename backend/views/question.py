from django.shortcuts import render
from backend.serializers.question import QuestionSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.question import Question
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class QuestionModelViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['QuestionId','QuestionType','SeId']
    search_fields=['QuestionId','QuestionType','SeId']
    odering_fields=['QuestionId']
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]