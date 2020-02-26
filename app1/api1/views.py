from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Faculty
from .serializers import InitialRequestSerializer
# Create your views here.

class InitialRegistrationView(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = InitialRequestSerializer




