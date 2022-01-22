from socket import fromshare
from django import forms
from django.forms import ModelForm
from DVT_api.models import Users


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('state', 'name', 'guid', 'pwc_ppi', 'owner', 'owner_project', 'email_address', 'account_type')
        labels = {
            'state': '',
            'name': '',
            'guid': '',
            'pwc_ppi': '',
            'owner': '',
            'owner_project': '',
            'email_address': '',
            'account_type': '',
        }
        
        widgets = {
            'state': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Account Sate (active/inactive)'}),
            'name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'User Name'}),
            'guid': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'PwC guID'}),
            'pwc_ppi': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'PwC PPI Code'}),
            'owner': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Project Owner'}),
            'owner_project': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Project Name'}),
            'email_address': forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Requester Email Address'}),
            'account_type': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Account Type (internal/external)'}),
        }