from socket import fromshare
from django import forms
from django.forms import ModelForm
from DVT_api.models import EventApp


class UserForm(ModelForm):
    class Meta:
        model = EventApp
        fields = ('guid', 'team_name', 'ticket_number', 'account_type')
        labels = {
            'guid': '',
            'team_name': '',
            'ticket_number': '',
            'account_type': '',
        }
        
        widgets = {
            'guid': forms.TextInput(attrs={'class' : 'form-control','style':'border-color : orange', 'placeholder' : 'PwC GUID'}),
            'team_name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'User Team Name'}),
            'ticket_number': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Service NOW Ticket number'}),
            'account_type': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Internal/External User'}),
        }