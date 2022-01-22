from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id','state','name', 'guid', 'pwc_ppi', 'owner','owner_project','email_address','account_type')