import json
import requests
from datetime import date
import logging
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class ServiceNowAPICalls:

    def __init__(self):

        # proxies setup in case they exist
        self.proxies = {
            "http": "",
            "https": "",
        }

        # Authentication
        self.auth = HTTPBasicAuth("us_svc_knbot_01", "0b0TX333#?#00*)petN5%")

        self.headers = {
            "apikey": "l7e17a1cee3a9742d3ad2c715bf47ad45d",
            "apikeysecret": "dca9cbf9bc704190a6c61e17433c4a0e",
            "Proxy-Authorization": "Basic VVNfaWZzX1hEUF9QbGF0Zm9ybV9PcGVyYXRpb25zX1JlcG9ydF9CdWlsZGVyX3AwMDE6ZEkzMTExdUROMWoxRjFzVzFJMW0=",
            "Accept": "application/json;charset=utf-8",
            "Content-Type": "application/json"
        }


        #close_task_uri = "https://api-sit.pwc.com/pwcnetwork/dev_2/service_now/api/now/table/sc_task/"
        #ritm_url = "/pwcnetwork/service_now/api/now/table/sc_req_item?sysparm_query=number%3D{}&sysparm_limit=1".format(sys.argv[1])
        #self.uri = "/pwcnetwork/service_now/api/now/table/sc_req_item?sysparm_query=number%3DRITM00001&sysparm_limit=1"
        self.uri = " https://api.pwc.com/pwcnetwork/service_now//api/now/table/sc_req_item"
        self.today_date = date.today()

    # Create RQ Item function
    def create_sc_req_item(self, guid=None, project=None, email=None, username=None):

        payload = {
        "sysparm_quantity": 1,
        "variables": {
            "container_start":"x",
            "requested_for":"{}".format(username),
            "Requester_Email":"{}".format(email),
            "tool": "GitHub",
            "Request_Type": "Add_User_To_Github",
            "Type_of_Access":"Add_User",
            "GUID":"{}".format(guid),
            "formatter":"x",
            "project": "{}".format(project),
            "date_needed": "{}".format(self.today_date),
            "wbs_code":"XXXAUTOMATION",
            "Role":"Developer",
            "other":"x",
            "formatter2":"x",
            "Comments":"This REQUEST was created by automation".
            }
        }

        response = requests.post(url=self.uri, data=json.dumps(payload), auth=self.auth,
                                 verify=False, headers=self.headers)
        content = response.json()
        assert (response.status_code == 200)
        if response.status_code == 200:
            print("Response Status Code: " + str(response.status_code))
            print("Response JSON Content: " + str(content))
            return Response({'Success!': 'RITM created successfully'},
                            status=HTTP_200_OK)
        else:
            return Response({'error': 'An error occurred, RITM was not created'},
                            status=HTTP_400_BAD_REQUEST)


    def get_active_task_from_current_ritm(self, ticket=None):

        get_active_task_url = "https://api-sit.pwc.com/pwcnetwork/dev_2/service_now/api/now/table/sc_task" \
                              "?sysparm_query=active%3Dtrue%5Erequest_item.number%3D{}&sysparm_fields" \
                              "=sys_id,number ".format(ticket)
        response = requests.get(url=get_active_task_url, auth=self.auth, verify=False, headers=self.headers)
        content = response.json()


