# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.forms import ValidationError,TextInput, PasswordInput


# class LoginForm(AuthenticationForm):
    
#     username = forms.EmailField(max_length=30, required=True, label="Email Address", widget=TextInput(attrs={
#         'autofocus': True,
#         'class' : 'span2',
#         'placeholder':'Email : ',
#     }))
    
#     password = forms.CharField(widget=PasswordInput(attrs={
#         'autocomplete': 'current-password',
#         'class': 'span2',
#         'placeholder':'Password : ',
#      }))


#     def clean(self):
#         email = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         user = None
#         try:
#             user = User.objects.get(email = email)
#             result = authenticate(username = user.username, password = password)
#             if(result is not None):
#                 return result
#             else:
#                 raise ValidationError("Email or Password Invalid")

#         except:
#             raise ValidationError("Email or Password Invalid")


from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate , login
from django.forms import ValidationError
from django.forms.widgets import PasswordInput, TextInput

class LoginForm(AuthenticationForm):
    


    username = forms.CharField(max_length=25 , required= True ,widget=TextInput(attrs={'autofocus': True,'class': 'span2','placeholder': 'Email',}))
    password = forms.CharField(widget=PasswordInput(attrs={'autocomplete': 'current-password','class': 'span2','placeholder':'Password', }))



    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user =  None
        try:
            user =  User.objects.get(email = email)
            result = authenticate(username = user.username , password = password)

            if(result is not None):
                return result
            else:
                 raise ValidationError("Email or Password Invalid")
        except:
            raise ValidationError("Email or Password Invalid")