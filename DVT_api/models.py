from asyncio.log import logger
from distutils.debug import DEBUG
from django import views
from django.db import models
#import lxml.etree as etree
from lxml import etree
from . import GUM_API
import logging
import time
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="/home/site/repository/logs/models.log",
                        level=logging.DEBUG, format=LOG_FORMAT)
logger=logging.getLogger()


class EventApp(models.Model):
    guid = models.CharField(max_length=60)
    team_name = models.CharField(max_length=60)
    ticket_number = models.CharField(max_length=60,blank=True, null=True)
    ppi_code = models.CharField(max_length=60)
    user_name =  models.CharField(max_length=120)
    email_address = models.EmailField(max_length=120)

        

    def save(self, *args, **kwargs):
        response = etree.parse("/home/site/repository/DVT_api/data.xml")
        if response is not None:
            #parsing the Envelope - XML response 
            xmlToString = etree.tostring(response, pretty_print = True)
            root = etree.fromstring(xmlToString)
            for child in root:
                pass
            for children in child:
                pass
            for children1 in children:
                #statusCode = children1[0].text
                self.email_address = children1[1][3].text
                self.user_name = children1[1][1].text + " " + children1[1][2].text
                special_attributes = children1[1][0][0][1]
            for attribute in special_attributes:
                self.ppi_code = attribute.text         
            super().save(*args, **kwargs)
        else:
            return Response({'error': '! Validation failure, record not saved to database....'},
                       status=HTTP_400_BAD_REQUEST)


def __str__(self):
            return str(self.guid)
    
        