from django.db import models
import xml.etree.ElementTree as ET
from . import GUM_API



class EventApp(models.Model):
    guid = models.CharField(max_length=60)
    team_name = models.CharField(max_length=60)
    ticket_number = models.CharField(max_length=60)
    account_type = models.CharField(max_length=120)
    ppi_code = models.CharField(max_length=60)
    user_name = models.CharField(max_length=120)
    email_address = models.EmailField(max_length=120)
    
       

    def save(self, *args, **kwargs):
        self.user_prod = 'US_GIHB_PROD_P001'
        self.password_prod = 'wML5Hu2CXPySuk3wGCJ6'
        self.groupGUID_Internal = 'gx_github_users_p001'
        self.gum_validate = GUM_API.GUM_Requests()
        self.gum_validate.ValidateUserByGuid(self.guid, self.password_prod, self.user_prod)
        self.response = GUM_API.xml
        if self.response is not None:
            self.root = ET.fromstring(self.response)
            for child in self.root: 
                pass
            for x in child:
                pass 
            for y in x:
                self.email_address = y[1][3].text
                self.user_name = y[1][1].text + " " + y[1][2].text




        super().save(*args, **kwargs)


 
    def __str__(self):
        return str(self.user_name)