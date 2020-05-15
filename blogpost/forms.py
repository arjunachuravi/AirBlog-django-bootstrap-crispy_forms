from django import forms
from .models import myprojectblog

class postform(forms.ModelForm):
    title = forms.CharField(
        max_length=50, required=True,
        widget = forms.TextInput(
            attrs= {
                "placeholder":"Here goes title",
                "class": "form-control",
            }
        )
    )
    desc = forms.CharField(
        max_length=100, required=True,
        widget = forms.Textarea(
            attrs={
                "placeholder":"Description goes here",
                "class":"form-control",
                "rows":"3"
            }
        )
    )
    tech = forms.CharField(
        max_length=50, required=True,
        widget = forms.TextInput(
            attrs={
                "placeholder":"Tech goes here",
                "class":"form-control"
            }
        )
    )
    class Meta:
        model = myprojectblog
        fields = [
            'title','desc','tech'
        ]