from rest_framework import serializers
from .models import EventApp

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventApp
        #fields = ('TeamName', 'Guid', 'WbsCode', 'TicketNumber', 'AccountType', 'UserName')
        fields = '__all__'
        extra_kwargs = {
            'guid' : {'required' : True, 'allow_blank' : False},
            'team_name' : {'required' : True, 'allow_blank' : False},
            'wbs_code' : {'required' : True, 'allow_blank' : False},
            'ticket_number' : {'required' : True, 'allow_blank' : False}
        }