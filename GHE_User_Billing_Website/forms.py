from socket import fromshare
from django import forms
from django.forms import ModelForm
from DVT_api.models import EventApp


class UserForm(ModelForm):
    class Meta:
        model = EventApp
        fields = ('guid', 'team_name', 'wbs_code', 'ticket_number', 'account_type')
        labels = {
            'Guid': '',
            'team_name': '',
            'wbs_code': '',
            'ticket_number': '',
            'account_type': '',
        }
        
        widgets = {
            'guid': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'PwC GUID'}),
            'team_name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'User Team Name'}),
            'wbs_code': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'WBS - Billing Code'}),
            'ticket_number': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Service NOW Ticket number'}),
            'account_type': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Internal/External User'}),
        }