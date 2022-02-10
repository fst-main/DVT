from django.db import models



class Detailed_User(models.Model):
    ppiCode = models.CharField(max_length=120)
    username = models.CharField(max_length=60)
    addedDate = models.DateTimeField('Added Date',max_length=120, blank =True)
    email_address = models.EmailField('Email Address', max_length=120) 
  

class Users(models.Model):
    requestedApp = models.CharField(max_length=60) #change the lenght
    guid = models.CharField(max_length=60)
    name = models.ForeignKey(Detailed_User, blank=True, null=True)
    teamName = models.CharField(max_length=60)
    wbsCode = models.CharField(db_column='pwc_ppi', max_length=60)  
    ticketNumber = models.CharField(max_length=60)
    accountType = models.CharField(max_length=120)
    

   
#modify the serializers, views , forms
#add new model for 
#make migrations

    
    def __str__(self):
        return self.username