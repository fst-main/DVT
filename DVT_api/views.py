from urllib import response
from flask import request
from itsdangerous import serializer
from sqlalchemy import true
from uritemplate import partial
from .serializers import UserSerializer
#from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import xml.etree.ElementTree as ET
from .models import EventApp
from .import GUM_API
import logging
import requests
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


groupGUID_Internal = 'gx_github_users_p001'
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\DevOpsTools_Automation\\Automation%20Platform\\logs\\models.log",
                        level=logging.DEBUG, format=LOG_FORMAT)
logger=logging.getLogger()




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
            guid = serializer.validated_data['guid']
            logger.info(f"Validating GUID: {guid}")
            validate = GUM_API.GUM_Requests()
            validate.ValidateUserByGuid(guid)
            serializer.save()
          else:
            logger.error(f"Invalid GUID: {guid}")
            return Response({'error': 'Invalid GUID'},
                        status=HTTP_404_NOT_FOUND)


            
          '''     
              addUser = GUM_API.GUM_Requests()
              addUser.AddGroupMember(groupGUID_Internal, guid, password_prod, user_prod)
            #need to check the response
                return Response({"status": "Success [ User was added to - gx_github_users_p001 - group...]",
                                "data":serializer.data},
                                 status=status.HTTP_200_OK)  
            '''     


@csrf_exempt
@api_view(["GET"])
def get_user(request):
        items = EventApp.objects.all()
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


 
