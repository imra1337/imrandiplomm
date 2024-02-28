from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, ValidationError, PasswordInput


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=TextInput(attrs={
        'class': 'span3',
        'placeholder': 'First Name',
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=TextInput(attrs={
        'class' : 'span3',
        'placeholder' : 'Last Name'
    }))
    username = forms.CharField(max_length=25, required=True, widget=TextInput(
        attrs={
            'class': 'span3',
            'placeholder' : 'Username'
        }
    ))
    email = forms.EmailField(max_length=30, required=True, label='Email Add',  widget=TextInput(attrs={
        'class': 'span3',
        'placeholder' : 'Email'
    }))

    def _init_(self, *args, **kwargs):
        super(UserCreationForm, self)._init_(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['password1'].label = 'Password :'
            self.fields['password2'].label = 'Confirm P:'
  
            self.fields['password1'].widget.attrs.update({'class' : 'span3', 'placeholder' : 'password'})
            self.fields['password2'].widget.attrs.update({'class' : 'span3' , 'placeholder' : 'Confirm password'})
    # def _init_(self, *args, **kwargs):
    #     super(UserCreationForm, self)._init_(*args, **kwargs)

    #     for fieldname in ['username', 'password1', 'password2']:
    #         self.fields[fieldname].help_text = None


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        user  = None
        try:
            user = User.objects.get(email = email)
        except:
            return email
        
        if(user is not None):
            raise ValidationError("User Email Already Exists");

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError
from django.forms.widgets import TextInput , PasswordInput

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=25 , required= True ,widget=TextInput(attrs={'class': 'span3','placeholder': 'First_Name'}))
    last_name = forms.CharField(max_length=25 , required= True ,widget=TextInput(attrs={'class': 'span3','placeholder': 'Last_Name'}))
    username = forms.CharField(max_length=25 , required= True ,widget=TextInput(attrs={'class': 'span3','placeholder': 'Username'}))
    email = forms.CharField(max_length=25 , required= True ,label='Email Add' ,widget=TextInput(attrs={'class': 'span3','placeholder': 'Email' }))
    
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['password1'].label = 'Password :'
            self.fields['password2'].label = 'Confirm P:'
  
            self.fields['password1'].widget.attrs.update({'class' : 'span3', 'placeholder' : 'password'})
            self.fields['password2'].widget.attrs.update({'class' : 'span3' , 'placeholder' : 'Confirm password'})


    # def _init_(self, *args, **kwargs):
    #     super(UserCreationForm, self)._init_(*args, **kwargs)

    #     for fieldname in ['username', 'password1', 'password2']:
    #         self.fields[fieldname].help_text = None
            # self.fields['password1'].label = 'Password :'
            # self.fields['password2'].label = 'Confirm P:'
  
            # self.fields['password1'].widget.attrs.update({'class' : 'span3', 'placeholder' : 'password'})
            # self.fields['password2'].widget.attrs.update({'class' : 'span3' , 'placeholder' : 'Confirm password'})



    class Meta:
        model = User
        fields = ['first_name'
         , 'last_name' , 'username'
          , "email" , 'password1'  , 'password2' ]
        
    def clean_email(self):
        email = self.cleaned_data['email']
        user  = None
        try:
            user = User.objects.get(email = email)
        except:
            return email
            
        if(user is not None):
            raise ValidationError("User Already Exists");
