from fileinput import close
from .serializers import UserSerializer
from rest_framework import status
import lxml.etree as etree
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import EventApp
from .import GUM_API
from .import SNow_API
import logging
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

#Global GUM variables
user_prod = 'US_GIHB_PROD_P001'
password_prod = 'wML5Hu2CXPySuk3wGCJ6'
groupGUID_Internal = 'gx_github_users_p001'

#logger configuration
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\DevOpsTools_Automation\\Automation%20Platform\\logs\\models.log",
                        level=logging.DEBUG, format=LOG_FORMAT)
logger=logging.getLogger()



#login function
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


#POST view function
@csrf_exempt
@api_view(["POST"])
def post_user(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            guid = serializer.validated_data['guid']
            team_name = serializer.validated_data['team_name']
            ticket = serializer.validated_data['ticket_number']
            logger.info(f"Validating GUID: {guid}")
            validate = GUM_API.GUM_Requests()
            validate.ValidateUserByGuid(guid)
            response = etree.parse("C:\\DevOpsTools_Automation\\Automation%20Platform\\DVT_api\\data.xml")
            xmlToString = etree.tostring(response, pretty_print=True)
            root = etree.fromstring(xmlToString)
            for child in root:
               pass
            for children in child:
               pass
            for children1 in children:
                try:
                    email_address = children1[1][3].text
                except IndexError:
                    print(f"GUID {guid} is not valid")
                    logger.info(f"GUID {guid} , is not valid...")
                    return Response({f"status": "error, invalid GUID!",
                            "data":serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

                user_name = children1[1][1].text + " " + children1[1][2].text
            if ticket == "":
                logger.info("Creating new ServiceNow ticket......")
                create_ritm = SNow_API.ServiceNowAPICalls()
                create_ritm.create_sc_ritm_item(guid, team_name, email_address, user_name)
                logger.info(f"RITM number: -----{SNow_API.ritm}-----")
                #add_user = GUM_API.GUM_Requests()
                #add_user.AddGroupMember(groupGUID_Internal, guid, password_prod, user_prod)
                get_active_task = SNow_API.ServiceNowAPICalls()
                get_active_task.get_active_task_from_current_ritm(SNow_API.ritm)
                close_ritm = SNow_API.ServiceNowAPICalls()
                close_ritm.close_record_active_task(SNow_API.task_sys_id)
                serializer.save()
                logger.info(f"User {user_name} saved to data base and added to GUM group")
                return Response({"status": "Success [ User was added to - gx_github_users_p001 - GUM group.",
                                 "data":serializer.data,
                                 "ticket_number": SNow_API.ritm},
                                       status=status.HTTP_200_OK)               
            else:
                add_user = GUM_API.GUM_Requests()
                add_user.AddGroupMember(groupGUID_Internal, guid, password_prod, user_prod)
                get_active_task = SNow_API.ServiceNowAPICalls()
                get_active_task.get_active_task_from_current_ritm(ticket)
                close_ritm = SNow_API.ServiceNowAPICalls()
                close_ritm.close_record_active_task(SNow_API.task_sys_id)
                logger.info(f"RITM number: -----{ticket}----- was closed!")
                serializer.save()
                logger.info(f"User {user_name} saved to data base and added to GUM group")
                return Response({"status": "Success [ User was added to - gx_github_users_p001 - GUM group.",
                            "data":serializer.data,
                            "ticket_number": ticket},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error",
                            "data":serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

#GET view function
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


 
