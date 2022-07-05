from socket import fromshare
from django import forms
from django.forms import ModelForm
from DVT_api.models import EventApp


class UserForm(ModelForm):
    class Meta:
        model = EventApp
        fields = ('guid', 'team_name', 'ticket_number')
        labels = {
            'guid': '',
            'team_name': '',
            'ticket_number': ''
        
        }
        
        widgets = {
            'guid': forms.TextInput(attrs={'class' : 'form-control','style':'border-color : orange', 'placeholder' : 'PwC GUID'}),
            'team_name': forms.TextInput(attrs={'class' : 'form-control', 'style':'border-color : orange',  'placeholder' : 'User Team Name'}),
            'ticket_number': forms.TextInput(attrs={'class' : 'form-control', 'style':'border-color : orange', 'placeholder' : 'Service NOW Ticket number'})
        }