from rest_framework import serializers
from .models import EventApp

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventApp
        fields = ('guid', 'team_name', 'ticket_number')