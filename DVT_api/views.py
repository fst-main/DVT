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
#from rest_framework.views import APIView
import xml.etree.ElementTree as ET
from .models import EventApp
from . import GUM_API
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
            guid = serializer.validated_data['guid']
            print(guid)
            account_type = serializer.validated_data['account_type']
            user_prod = 'US_GIHB_PROD_P001'
            password_prod = 'wML5Hu2CXPySuk3wGCJ6'
            groupGUID_Internal = 'gx_github_users_p001'
            groupGUID_External = 'gx_github_ext_users_p001'
            

            if (account_type != 'Internal' or account_type != 'internal' and account_type !='external' or account_type != 'External'):
                return Response({"status": "error",
                           "data":serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

            #switch between internal or external 
            else:
                if (account_type == 'Internal' or account_type == 'internal'): 
                #add user to GUM
                    addUser = GUM_API.GUM_Requests()
                    addUser.AddGroupMember(groupGUID_Internal, guid, password_prod, user_prod)
                    serializer.save()
                    return Response({"status": "Success [ User was aded as an internal user...]",
                            "data":serializer.data},
                            status=status.HTTP_200_OK)
                else:
                    addUser = GUM_API.GUM_Requests()
                    addUser.AddGroupMember(groupGUID_External, guid, password_prod, user_prod)
                    serializer.save()
                    return Response({"status": "Success [ User was aded as an external user...]",
                            "data":serializer.data},
                            status=status.HTTP_200_OK)
        root = ET.fromstring(GUM_API.xml)
        for child in root: 
            pass
        for x in child:
            pass
        for y in x:
            status = y[0].text
            FirstName = y[1][1].text
            SecondName = y[1][2].text
            EmailAddress = y[1][3].text
            FullName = FirstName + " " + SecondName
            print("Email Address: ",EmailAddress)
            print ("Fullname: ", FullName)
            FullName.save(update_fields=['user_name'])
            EmailAddress.save(update_fields=['email_address'])




            
       
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


 
