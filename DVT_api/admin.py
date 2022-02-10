from django.contrib import admin
from .models import Atlassian, AzureDevOps, EventApp, GitHub, PwC_User


admin.site.register(EventApp)
admin.site.register(GitHub)
admin.site.register(AzureDevOps)
admin.site.register(Atlassian)
admin.site.register(PwC_User)
