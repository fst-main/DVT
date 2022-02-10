from django.db import models

class Users(models.Model):
    requestedApp = models.CharField(max_length=60) #change the lenght
    username = models.CharField(max_length=60)
    teamName = models.CharField(max_length=60)
    guid = models.CharField(max_length=60)
    wbsCode = models.CharField(db_column='pwc_ppi', max_length=60)  
    ticketNumber = models.CharField(max_length=60)
    email_address = models.CharField(max_length=120)
    accountType = models.CharField(max_length=120)

   
#modify the serializers, views , forms
#add new model for 
#make migrations

    
    def __str__(self):
        return self.username