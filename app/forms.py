from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    cpassword=forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    def clean(self):
        usr=super().clean()
        if(usr['password']!=usr['cpassword']):
            raise forms.ValidationError("Passwords do not match!")
    class Meta():
        model=User
        fields = ('first_name','last_name','email','username','password','cpassword')
        widgets = {
            'first_name':forms.TextInput(),
            'last_name':forms.TextInput(),
            'email':forms.EmailInput(),
            'username':forms.TextInput(),
            'password':forms.PasswordInput()
        }


class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields = ('dob','gender','profile_pic')
        labels={
            'dob':'DOB',
            'gender':'Gender',
            'profile_pic':'Profile Picture'
        }
        widgets={
            'dob':forms.DateInput(format=('%d-%m-%Y'),attrs={'type': 'date'}),
            'gender':forms.Select(choices=((False,'Male'),(True,'Female'))),
            'profile_pic':forms.FileInput(),
        }