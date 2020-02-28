from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from .models import Faculty
from .serializers import InitialRequestSerializer, LoginResponseSerializer, initialRegistrationResponseSerilaizer


class APIResponse():
    def __init__(self, code, msg, data):
        self.status_code = code
        self.status_message = msg
        self.data = data


class InitialRegistrationView(APIView):
    def post(self, request):
        data = {
            "name": "adi",
            "email_id": "adithyaq111326@gmail.com",
            "password": "adi",
            "department": "ISE",
            "faculty_type": [{"type_description": "P"}]
        }
        # serilalizer = InitialRequestSerializer(data={"data" : request.data})
        serilalizer = initialRegistrationResponseSerilaizer(data={"data" : data})
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_200_OK)
        print(serilalizer.errors)
        return Response(serilalizer.errors, status=status.HTTP_401_UNAUTHORIZED)


class LoginView(APIView):
    def post(self, request):
        data = {
            'email_id': 'achsarwwe6@gmail.com',
            "password": 'adi'
        }
        # serializer = LoginSerializer(data=request.data)
        serializer = LoginResponseSerializer(data={"data": data})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(APIResponse(code=404, msg="Error", data=serializer.errors['data']).__dict__, status=status.HTTP_200_OK)
