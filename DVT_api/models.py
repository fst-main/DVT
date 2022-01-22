from django.db import models

class Users(models.Model):
    state = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    guid = models.CharField(max_length=60)
    pwc_ppi = models.CharField(db_column='pwc_ppi', max_length=60)  # Field name made lowercase.
    owner = models.CharField(max_length=60)
    owner_project = models.CharField(db_column='owner_project', max_length=60)  # Field name made lowercase.
    email_address = models.CharField(max_length=120)
    account_type = models.CharField(db_column='account_type', max_length=60)  # Field name made lowercase.

    
    def __str__(self):
        return self.name