from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from .models import Faculty
from .serializers import InitialRequestSerializer
from .serializers import FinalRequestSerializer


class InitialRegistrationView(APIView):
    def post(self, request):
        serilalizer = InitialRequestSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_200_OK)
        print(serilalizer.errors)
        return Response(serilalizer.errors, status=status.HTTP_401_UNAUTHORIZED)



class FinalRegistrationView(APIView):
    def post(self, request):
        serilalizer = FinalRequestSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_200_OK)
        print(serilalizer.errors)
        return Response(serilalizer.errors, status=status.HTTP_401_UNAUTHORIZED)
