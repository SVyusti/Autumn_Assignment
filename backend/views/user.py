from django.shortcuts import render
from backend.serializers.user import UserSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.user import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserModelViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['name','EnrollmentNo','username','year']
    search_fields=['name','EnrollmentNo','year','username']
    odering_fields=['name','EnrollmentNo']
    # permission_classes=[IsAuthenticated]