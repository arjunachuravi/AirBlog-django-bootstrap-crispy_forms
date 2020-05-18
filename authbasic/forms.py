from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = [
            'email','username','password',
        ]