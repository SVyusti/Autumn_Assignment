from django.shortcuts import render
from backend.serializers.section import SectionSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.section import Section
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class SectionModelViewSet(viewsets.ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields="__all__"
    search_fields=['S_Id','role']
    odering_fields=['RoundId','S_Id','type']
    odering=['RoundId']
    # authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]