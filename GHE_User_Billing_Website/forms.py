from socket import fromshare
from django import forms
from django.forms import ModelForm
from DVT_api.models import EventApp


class UserForm(ModelForm):
    class Meta:
        model = EventApp
        fields = ('guid', 'teamName', 'wbsCode', 'ticketNumber', 'accountType')
        labels = {
            'guid': '',
            'teamName': '',
            'wbsCode': '',
            'ticketNumber': '',
            'accountType': '',
        }
        
        widgets = {
            'guid': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'PwC GUID'}),
            'teamName': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'User Team Name'}),
            'wbsCode': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'WBS - Billing Code'}),
            'ticketNumber': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Service NOW Ticket number'}),
            'accountType': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Internal/External User'}),
        }