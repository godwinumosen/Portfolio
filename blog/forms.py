from django import forms
from .models import UserModel



class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['fistname', 'lastname','email','password','confirm_password']
