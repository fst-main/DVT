from rest_framework import serializers
from .models import EventApp

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventApp
        fields = ('teamName', 'guid', 'wbsCode', 'ticketNumber', 'accountType')