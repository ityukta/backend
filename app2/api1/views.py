from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Faculty
from .serializers import InitialRequestSerializer
# Create your views here.


class InitialRegistrationView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Faculty.objects.all()
    serializer_class = InitialRequestSerializer

        