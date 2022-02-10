from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('requestedApp','username','teamName', 'guid', 'wbsCode', 'ticketNumber', 'email_address', 'accountType')