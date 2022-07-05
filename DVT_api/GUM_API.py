import requests
import bs4
from bs4 import BeautifulSoup
import tkinter 
from tkinter import Tk, Label, Button, Entry
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from xml.etree import cElementTree as ET


#globals 
#user_stage = 'US_GIHB_STG_S001'

#password_stage = 'e9BVRCbRN6ZmxaVHAgdp'

#endpoint_stage = "https://gumapiservice-stage.pwcinternal.com/GumService.asmx"


xml = None
user_prod = 'US_GIHB_PROD_P001'
password_prod = 'wML5Hu2CXPySuk3wGCJ6'
endpoint_prod = "https://gumapiservice.pwcinternal.com/GumService.asmx?wsdl"
headers = {"Content-Type" : "text/xml"}


class GUM_Requests:


#validate user by GUID
    def ValidateUserByGuid (self,GuidParameter = None):
        body = '''<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ValidateUserByGuid xmlns="http://pwcinternal.com/">
      <guid>{guid}</guid>
      <myCred>
        <password>{password}</password>
        <userName>{user}</userName>
      </myCred>
    </ValidateUserByGuid>
  </soap:Body>
</soap:Envelope>'''

        body = body.format(guid = GuidParameter, password = password_prod, user = user_prod)
        body = body.encode('utf-8')
        session = requests.session()
        session.headers = headers
        response  =  session.post(url = endpoint_prod, data = body, verify=False)
        global xml
        xml = response.content
        with open("C:\\DevOpsTools_Automation\\Automation%20Platform\\DVT_api\\data.xml", 'wb') as data_xml:
                data_xml.write(xml)

       
#validate user by Email address 
    def ValidateUserByEmail(self, EmailParameter = None, PasswordParameter = None, UserParameter = None ):

        body = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ValidateUserByEmail xmlns="http://pwcinternal.com/">
      <email>{email}</email> 
      <myCred>
        <password>{password}</password>
        <userName>{user}</userName>
      </myCred>
    </ValidateUserByEmail>
  </soap:Body>
</soap:Envelope>'''

        body = body.format(email = EmailParameter, password = PasswordParameter, user = UserParameter )
        body = body.encode('utf-8')
        session = requests.session()
        session.headers = headers
        response  =  session.post(url = endpoint_prod, data = body, verify=False)
        global xml
        xml = response.content
        

#AddGroupMember method
    def AddGroupMember(self,GroupGuidParameter = None, GuidParameter = None, PasswordParameter = None, UserParameter = None):

        body = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <AddGroupMember xmlns="http://pwcinternal.com/">
      <groupGuid>{goupGUID}</groupGuid>
      <guidsToAdd>
        <string>{guid}</string>
      </guidsToAdd>
      <myCred>
        <password>{password}</password>
        <userName>{user}</userName>
      </myCred>
    </AddGroupMember>
  </soap:Body>
</soap:Envelope>'''

        body = body.format(goupGUID = GroupGuidParameter,guid = GuidParameter, password = PasswordParameter, user = UserParameter)
        body = body.encode('utf-8')
        session = requests.session()
        session.headers = headers
        response  =  session.post(url = endpoint_prod, data = body, verify=False)
        global xml
        xml = response.content
        
        

#RemoveGroupMember method
    def RemoveGroupMember (self,GroupGuidParameter = None, GuidParameter = None, PasswordParameter = None, UserParameter = None):

        body = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <RemoveGroupMember xmlns="http://pwcinternal.com/">
      <groupGuid>{goupGUID}</groupGuid>
      <guidsToRemove>
        <string>{guid}</string>
      </guidsToRemove>
      <myCred>
        <password>{password}</password>
        <userName>{user}</userName>
      </myCred>
    </RemoveGroupMember>
  </soap:Body>
</soap:Envelope>'''


        body = body.format(goupGUID = GroupGuidParameter,guid = GuidParameter, password = PasswordParameter, user = UserParameter)
        body = body.encode('utf-8')
        session = requests.session()
        session.headers = headers
        response  =  session.post(url = endpoint_prod, data = body, verify=False)
        global xml
        xml = response.content
        
        



#create new user 

    def CreateNewUser(self, FirstNameParameter = None, LastNameParameter = None, EmailParameter = None, OrganizationParameter = None, territoryParameter = None, PasswordParameter = None, UserParameter = None ):

        body = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CreateUser xmlns="http://pwcinternal.com/">
      <gmUser>
        <FirstName>{FirstName}</FirstName>
        <LastName>{LastName}</LastName>
        <Email>{email}</Email>
        <Organization>{organization}</Organization>
        <Territory>{territory}</Territory>
      </gmUser>
      <myCred>
        <password>{password}</password>
        <userName>{user}</userName>
      </myCred>
    </CreateUser>
  </soap:Body>
</soap:Envelope>'''

        body = body.format(FirstName = FirstNameParameter, LastName = LastNameParameter,  email = EmailParameter, organization = OrganizationParameter,territory = territoryParameter, password = PasswordParameter, user = UserParameter)
        body = body.encode('utf-8')
        session = requests.session()
        session.headers = headers
        response  =  session.post(url = endpoint_prod, data = body, verify=False)
        global xml
        xml = response.content
        
        

#get Application names

    def GetApplicationNames (self, PasswordParameter = None, UserParameter = None):

        body  = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetApplicationNames xmlns="http://pwcinternal.com/">
      <myCred>
        <password>{password}</password>
        <userName>{user}</userName>
      </myCred>
    </GetApplicationNames>
  </soap:Body>
</soap:Envelope>'''

        body = body.format(password = PasswordParameter, user = UserParameter)
        body = body.encode('utf-8')
        session = requests.session()
        session.headers = headers
        response  =  session.post(url = endpoint_prod, data = body, verify=False)
        global xml
        xml = response.content
        




class ADD_GUI(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("GUM Operations")
        self.geometry('960x600')
        self.configure(background = 'black')

#---------------------------------------------------------VALIDATE USER--------------------------------------------------------------------------------

#Validate user label
        self.label1  = Label(self, text = "Validate User :", font = "Veranda 11 bold", fg = "yellow2", bg = "black" )
        self.label1.place(relx = 0.09, rely=0.10, anchor = 'sw')
#Validate user label
        self.label_guid  = Label(self, text = "GUID / Email:", fg= "white", font = "Veranda 9 bold", bg = "black" )
        self.label_guid.place(relx = 0.09, rely=0.15, anchor = 'sw')
#Validate user GUID entry 
        self.entry_guid = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_guid.place(relx = 0.20, rely=0.15, anchor = 'sw')
#Validate guid button 
        self.button_validateUser = Button(self, text = "   Validate   ", bg = "grey85" ,height = 1, command = self.ValidationOptions)
        self.button_validateUser.place (relx = 0.25, rely=0.21, anchor = 'sw')


# -------------------------------------------------------CREATE USER----------------------------------------------------------------------------------

#Create user Label 
        self.label2  = Label(self, text = "Create User :", font = "Veranda 11 bold", fg = "yellow2", bg = "black" )
        self.label2.place(relx = 0.09, rely=0.26, anchor = 'sw')
#Create user - First Name -Label
        self.label_fname  = Label(self, text = "First Name :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_fname.place(relx = 0.09, rely=0.30, anchor = 'sw')
#Create user - Last Name - Label
        self.label_lname  = Label(self, text = "Last Name :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_lname.place(relx = 0.09, rely=0.35, anchor = 'sw')
#Create user - email  - Label
        self.label_email_add = Label(self, text = "Email :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_email_add.place(relx = 0.09, rely=0.40, anchor = 'sw')
#Create user - Organization - Label
        self.label_organisation  = Label(self, text = "Organisation :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_organisation.place(relx = 0.09, rely=0.45, anchor = 'sw')
#Create user - Territory  - Label 
        self.label_territory  = Label(self, text = "Territory :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_territory.place(relx = 0.09, rely=0.50, anchor = 'sw')
#Create user - First Name -Entry 
        self.entry_fname = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_fname.place(relx = 0.20, rely=0.30, anchor = 'sw')
#Create user - Last Name - Entry 
        self.entry_lname = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_lname.place(relx = 0.20, rely=0.35, anchor = 'sw')
#Create user - Organization - Entry 
        self.entry_email_add = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_email_add.place(relx = 0.20, rely=0.40, anchor = 'sw')
#Create user - Organization - Entry 
        self.entry_organisation = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_organisation.place(relx = 0.20, rely=0.45, anchor = 'sw')
#Create user - Territory  - Entry 
        self.entry_territory = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_territory.place(relx = 0.20, rely=0.50, anchor = 'sw')
#Create User - Button 
        self.button_createUser = Button(self, text = "   Create User   ", bg = "grey85", height = 1,  command = self.CreateUser, relief=RAISED )
        self.button_createUser.place (relx = 0.25, rely=0.56, anchor = 'sw')

# -----------------------------------------------------ADD GROUP MEMBER -----------------------------------------------------------------------

#Gruoup Add Label
        self.label3  = Label(self, text = "Add Group Member :", font = "Veranda 11 bold", fg = "yellow2", bg = "black" )
        self.label3.place(relx = 0.09, rely=0.61, anchor = 'sw')
#Group Add GUID label
        self.label_guid_AddGroup  = Label(self, text = "gGUID :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_guid_AddGroup.place(relx = 0.09, rely=0.66, anchor = 'sw')
#Group Add Group  label
        self.label_guid_AddGroup  = Label(self, text = "GUID :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_guid_AddGroup.place(relx = 0.09, rely=0.71, anchor = 'sw')       
#Group Add Group GUID Entry 
        self.entry_gguid_AddGroup = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_gguid_AddGroup.place(relx = 0.20, rely=0.66, anchor = 'sw')
#Group Add Member GUID Entry 
        self.entry_guid_AddGroup = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_guid_AddGroup.place(relx = 0.20, rely=0.71, anchor = 'sw')


        self.button_AddGroup = Button(self, text = "Add Member", bg = "grey85" ,height = 1, command = self.AddGroupMember, relief=RAISED)
        self.button_AddGroup.place (relx = 0.25, rely=0.77, anchor = 'sw')

#------------------------------------------------REMOVE GROUP MEMBER-----------------------------------------------------------------------------

        self.label4  = Label(self, text = "Remove Group Member :", font = "Veranda 11 bold", fg = "yellow2", bg = "black" )
        self.label4.place(relx = 0.09, rely=0.82, anchor = 'sw')
#Group Remove Members  labels
        self.label_guid_RMVgroup  = Label(self, text = "gGUID :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_guid_RMVgroup.place(relx = 0.09, rely=0.87, anchor = 'sw')

        self.label_guid_RMVgroup  = Label(self, text = "GUID :", fg= "white", font = "Veranda 10 bold", bg = "black" )
        self.label_guid_RMVgroup.place(relx = 0.09, rely=0.92, anchor = 'sw')
#Group Remove Members  Entry
        self.entry_gguid_RMVgroup = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_gguid_RMVgroup.place(relx = 0.20, rely=0.87, anchor = 'sw')

        self.entry_guid_RMVgroup = Entry(self, bg = "grey79", bd = 0, width = 30)
        self.entry_guid_RMVgroup.place(relx = 0.20, rely=0.92, anchor = 'sw')
#Group Remove Members  Button
        self.button_RMVgroup = Button(self, text = "  Rmv Member  ", bg = "grey85" ,height = 1, command = self.RmvGroupMember, relief=RAISED)
        self.button_RMVgroup.place (relx = 0.25, rely=0.98, anchor = 'sw')

# ------------------------------------------------APPLICATION NAMES -----------------------------------------------------------------------------   

        button_getAppNames = Button(self, text = "Get Application Names", bg = "grey85" ,height = 1, width = 40, command = self.update, relief=RAISED)
        button_getAppNames.place (relx = 0.53, rely=0.92, anchor = 'sw')


#-------------------------------------------------API RESPONSE------------------------------------------------------------------------------------
        self.label5  = Label(self, text = "API Response :", font = "Veranda 11 bold", fg = "yellow2", bg = "black" )
        self.label5.place(relx = 0.45, rely=0.10, anchor = 'sw')
#-------------------------------------------------TEXT WIDGET-------------------------------------------------------------------------------------
        self.textWidget = Text(self, relief='flat', bg = 'grey79', highlightthickness=0, height=27, width=55)
        self.textWidget.bind("<1>", lambda event: self.textWidget.focus_set())
        self.textWidget.insert('1.0', "")
        self.textWidget.configure(state="disabled", inactiveselectbackground=self.textWidget.cget("selectbackground"))
        self.textWidget.place(relx = 0.45, rely=0.85, anchor = 'sw')
#Scroll bar 

        scrollbar = ttk.Scrollbar(self,command = self.textWidget.yview)
        scrollbar.place(relx = 0.92, rely=0.53, anchor = 'sw')
        self.textWidget['yscrollcommand'] = scrollbar.set


#Main loop 
        self.mainloop()

    def updateTextWidget(self,new_text):
        self.textWidget.configure(state = 'normal')
        self.textWidget.delete('1.0','end')
        self.textWidget.insert('1.0', new_text)
        self.textWidget.configure(state = 'disabled')

    def update(self):
        app = GUM_Requests()
        app.GetApplicationNames(password_prod,user_prod)
        parsedXML = BeautifulSoup(xml, 'xml')
        parsedXML = parsedXML.prettify()
        print("\n")
        print (parsedXML)  
        self.updateTextWidget(parsedXML)
  
    def ValidationOptions(self):
        validate = self.entry_guid.get()
        if (len(validate) == 0):
            messagebox.showerror("Validation Error", "Fields are empty!")   
        else:
            if '@' in validate:
                app = GUM_Requests()
                app.ValidateUserByEmail(validate,password_prod,user_prod)
                parsedXML = BeautifulSoup(xml, 'xml')
                parsedXML = parsedXML.prettify()
                self.updateTextWidget(parsedXML)
            else:
                app=GUM_Requests()
                app.ValidateUserByGuid(validate,password_prod,user_prod)
                parsedXML = BeautifulSoup(xml, 'xml')
                parsedXML = parsedXML.prettify()
                self.updateTextWidget(parsedXML)

    def AddGroupMember(self):
        addGroupID = self.entry_gguid_AddGroup.get()
        addMember = self.entry_guid_AddGroup.get()
        app = GUM_Requests()
        app.AddGroupMember(addGroupID,addMember,password_prod,user_prod)
        parsedXML = BeautifulSoup(xml, 'xml')
        parsedXML = parsedXML.prettify()
        self.updateTextWidget(parsedXML)


    def RmvGroupMember (self):
        rmvGroupID = self.entry_gguid_RMVgroup.get()
        rmvMember = self.entry_guid_RMVgroup.get()
        app = GUM_Requests()
        app.RemoveGroupMember(rmvGroupID ,rmvMember,password_prod,user_prod)
        parsedXML = BeautifulSoup(xml, 'xml')
        parsedXML = parsedXML.prettify()
        self.updateTextWidget(parsedXML)

    def CreateUser (self):
        firstName = self.entry_fname.get()
        lastName = self.entry_lname.get()
        email = self.entry_email_add.get()
        organization = self.entry_organisation.get()
        territory = self.entry_territory.get()
        app = GUM_Requests()
        app.CreateNewUser(firstName, lastName, email, organization, territory, password_prod, user_prod )
        parsedXML = BeautifulSoup(xml,'xml')
        parsedXML = parsedXML.prettify()
        self.updateTextWidget(parsedXML)



if __name__ == '__main__':
    gum_app = ADD_GUI()
