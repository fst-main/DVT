from django.db import models



class GitHub(models.Model):
    name = models.CharField('Github',max_length=60)
    ppiCode = models.CharField(max_length=120)
    addedDate = models.DateTimeField('Added Date',max_length=120, blank =True)
    email_address = models.EmailField('Email Address', max_length=120) 
    
    def __str__(self):
        return self.name

class AzureDevOps(models.Model):
    name = models.CharField('Azure DevOps',max_length=60)
    addedDate = models.DateTimeField('Added Date',max_length=120, blank =True)
    email_address = models.EmailField('Email Address', max_length=120)
    
    def __str__(self):
        return self.name

class Atlassian(models.Model):
    name = models.CharField('Atalssian',max_length=60)
    addedDate = models.DateTimeField('Added Date',max_length=120, blank =True)
    email_address = models.EmailField('Email Address', max_length=120)

    def __str__(self):
        return self.name

class PwC_User(models.Model):
    username = models.CharField(max_length=120)

    def __str__(self):
        return self.username


class EventApp(models.Model):
    requestedApp_Git = models.ForeignKey(GitHub, blank=True, null=True, on_delete=models.CASCADE)
    requestedApp_Ado = models.ForeignKey(AzureDevOps, blank=True, null=True, on_delete=models.CASCADE)
    requestedApp_Atl = models.ForeignKey(Atlassian, blank=True, null=True, on_delete=models.CASCADE)
    #requestedApp = 
    name = models.CharField('Application Name',max_length=60,blank=True)
    guid = models.CharField(max_length=60)
    teamName = models.CharField(max_length=60)
    wbsCode = models.CharField(db_column='pwc_ppi', max_length=60)  
    ticketNumber = models.CharField(max_length=60)
    accountType = models.CharField(max_length=120)
    TablesConnector = models.ManyToManyField(PwC_User, blank=True)
    
       
    def __str__(self):
        return self.name