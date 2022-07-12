import json
import requests
from datetime import date
import logging
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response
from requests.adapters import HTTPAdapter
from urllib3 import Retry
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

task_sys_id = None
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\DevOpsTools_Automation\\Automation%20Platform\\logs\\models.log",
                    level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()

class ServiceNowAPICalls:

    def __init__(self):

        # proxies setup in case they exist
        self.proxies = {
            "http": "",
            "https": "",
        }

        # Authentication
        self.auth = HTTPBasicAuth("gbl_svc_githubgum_01", "g#K9yJuH7*4%E5nWx")

        self.headers = {
            "apikey": "l77f357e42819e431a9e4730b4daf36cb0",
            "apikeysecret": "aa298cc24ac44fb7a29b2566a0a76df7",
            "Proxy-Authorization": "Basic VVNfaWZzX0dpdEhVQl90b19TTk9XX0ludGVncmF0aW9uX3AwMDE6RmElSS95R0BYdlpGPXEjLjAuWCo=",
            "Accept": "application/json;charset=utf-8",
            "Content-Type": "application/json"
        }
        self.req_uri = "https://api.pwc.com/pwcnetwork/service_now/api/sn_sc/servicecatalog/items" \
                   "/d954573ddbe53340a416f5261d9619c0/order_now"
        self.ritm_uri = "https://api.pwc.com/pwcnetwork/service_now/api/ipwc/request_item/create/d954573ddbe53340a416f5261d9619c0/ritm_nv"
        self.today_date = date.today()

        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.auth = self.auth
        self.retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "POST", "OPTIONS"]
        )
        self.adapter = HTTPAdapter(max_retries=self.retry_strategy)
        self.session.mount("https://", self.adapter)
        self.session.mount("http://", self.adapter)
        self.assert_status_hook = lambda response, *args, **kwargs: response.raise_for_status()
        self.session.hooks["response"] = [self.assert_status_hook]





    #Get the task ID from current RITM
    def get_active_task_from_current_ritm(self, ritm=None):
        get_active_task_url = "https://api.pwc.com/pwcnetwork/service_now/api/now/table/sc_task?sysparm_query=active" \
                              "%3Dtrue%5Erequest_item.number%3D{}&sysparm_fields=sys_id,number".format(ritm)
        response = requests.get(url=get_active_task_url, auth=self.auth, verify=False, headers=self.headers)
        content = response.json()
        global task_sys_id
        task_sys_id = content['result'][0]['sys_id']
        print("Task SysID :", task_sys_id)


    #Close the RITM using the task_id
    def close_record_active_task(self, task_sys_id=None):
        uri = "https://api.pwc.com/pwcnetwork/service_now/api/now/table" \
              "/sc_task/{}".format(task_sys_id)
        payload = {
            "state":"3",
            "active":"false"
        }
        response = self.session.patch(url=uri, data=json.dumps(payload), auth=self.auth,
                                 verify=False, headers=self.headers)
        if response.status_code == 200 or response.status_code == 201:
            print("Success! RITM closed successfully....")
        else:
            print("Error! An error occurred, RITM was not closed.....")



    # Create REUEST Item function
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
            "Comments":"This REQUEST was created by automation"
            }
        }
        response = self.session.post(url=self.req_uri, data=json.dumps(payload), auth=self.auth,
                                    verify=False, headers=self.headers)
        content = response.json()
        if response.status_code == 200:
            print("Response JSON Content: " + str(content))
            return Response({'Success!': 'REQUEST created successfully'},
                            status=HTTP_200_OK)
        else:
            return Response({'error': 'An error occurred, REQUEST was not created'},
                            status=HTTP_400_BAD_REQUEST)


    #Create sc_RITM_item function
    def create_sc_ritm_item(self, guid=None, project=None, email=None, username=None):
        logger.info("Creating new RITM.....")
        payload = {
        "sysparm_quantity": 1,
        "variables": {
            "container_start": "x",
            "requested_for": "{}".format(username),
            "Requester_Email": "{}".format(email),
            "tool": "GitHub",
            "Request_Type": "Add_User_To_Github",
            "Type_of_Access": "Add_User",
            "GUID": "{}".format(guid),
            "formatter": "x",
            "project": "{}".format(project),
            "date_needed": "{}".format(self.today_date),
            "wbs_code": "XXXAUTOMATION",
            "Role": "Developer",
            "other": "x",
            "formatter2": "x",
            "Comments": "This REQUEST was created by DevOps Tools automation and it will be closed automatically"
            }
        }
        response = self.session.post(url=self.ritm_uri, data=json.dumps(payload), auth=self.auth,
                                     verify=False, headers=self.headers)
        content = response.json()
        if response.status_code == 200 or response.status_code == 201:
                print("Response JSON Content: " + str(content))
                ritm = content['result']['record']
                print("Ritm number: ", ritm)
                logger.info(f"RITM {ritm} was created...")
                print("Success! RITM created successfully.......")
                self.get_active_task_from_current_ritm(ritm)
                self.close_record_active_task(task_sys_id)
                print("Success! RITM closed successfully.......")
                
        else:
                print("Error! An error occurred, RITM was not created.....")