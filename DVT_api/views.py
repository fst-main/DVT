from flask import request
from itsdangerous import serializer
from sqlalchemy import true
from uritemplate import partial
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def post_user(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                            "data":serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error",
                            "data":serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
def get_user(request):
        items = Users.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response({"status": "success", 
                            "data": serializer.data},  
  
  
  
  
                            status=status.HTTP_200_OK)
"""
def patch():
        item = Users.objects.get(id=id)
        serializer = UserSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


def delete(request, id=None):
        item = get_object_or_404(Users, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
"""


 
