from rest_framework import serializers
from .models import EventApp

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventApp
        fields = ('account_type', 'guid', 'team_name', 'wbs_code', 'ticket_number')