from django.db import models



class EventApp(models.Model):
    guid = models.CharField(max_length=60)
    team_name = models.CharField(max_length=60)
    wbs_code = models.CharField(max_length=60)  
    ticket_number = models.CharField(max_length=60)
    account_type = models.CharField(max_length=120)
    ppi_code = models.CharField(max_length=60)
    user_name = models.CharField(max_length=120)
    email_address = models.EmailField(max_length=120)
    
       
    def __str__(self):
        return str(self.guid)