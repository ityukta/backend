from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Faculty
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny

class APIResponse():
    def __init__(self, code, msg, data):
        self.status_code = code
        self.status_message = msg
        self.data = data


class InitialRegistrationView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        # data = {
        #     "name": "adi",
        #     "email_id": "adithyaqaaa111326@gmail.com",
        #     "password": "adi",
        #     "department": "ISE",
        #     "faculty_type": [{"type_description": "P"}]
        # }
        # serilalizer = InitialRequestSerializer(data={"data" : data})
        data = list(dict(request.data).keys())[0]
        print(data)
        serilalizer = initialRegistrationResponseSerilaizer(data={"data" :eval(data)})
        if serilalizer.is_valid():
            serilalizer.save()
            print(serilalizer.data)
            return Response(serilalizer.data, status=status.HTTP_200_OK)
        print(serilalizer.errors)
        return 1


class LoginView(APIView):
    permission_classes = (AllowAny,)
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

class Completeregistrationview(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        data = list(dict(request.data).keys())[0]
        serializer = CompleteRegistrationResponseSerializer(data={"data" :eval(data)})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(APIResponse(code=404, msg="Error", data=serializer.errors['data']).__dict__, status=status.HTTP_200_OK)


def initialRegister(request):
    return render(request, 'html/register1.html')

# @csrf_exempt
# def initialRegisterAjax(request):
#     print(request)
#     if request.method == "POST":
#         print(request.body)
#         return "what???"
#     print("not a post method")
#     return HttpResponse("not working")