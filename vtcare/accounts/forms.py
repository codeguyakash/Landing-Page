from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from.models import *

User = get_user_model()

class RegistrationForm(UserCreationForm):
    class Meta:
        model =Account
        fields = ['first_name', 'last_name', 'user_name', 'email','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        
        self.fields['user_name'].widget.attrs.update({'placeholder': 'User Name'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
        
        
        for fieldname in ['user_name', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        
        icons = {
            'first_name': 'fa-user',
            'last_name': 'fa-user',
            'user_name': 'fa-user',
            'email': 'fa-envelope',
            'password1': 'fa-lock',
            'password2': 'fa-lock'
        }
        for field_name, icon in icons.items():
            self.fields[field_name].icon = icon



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'query']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': ''}),
            'last_name': forms.TextInput(attrs={'placeholder': ''}),
            'email': forms.EmailInput(attrs={'placeholder': ''}),
            'phone_number': forms.TextInput(attrs={'placeholder': ''}),
            'query': forms.Textarea(attrs={'placeholder': 'Write your message here', 'rows': 4, 'cols': 15}),
        }
        
        
class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password=forms.CharField(max_length=15)
    confirm_password=forms.CharField(max_length=15)
        