from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class UserForm(forms.Form,forms.ModelForm):
    username = forms.CharField(
        max_length=50, required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username'
            } ) )
    password = forms.CharField(
        required=True,max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Tell the magic code'
            }  ) )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email'
            } ) )

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('username',css_class="form-group col-6"),
                css_class='form-row'
            ),
            Row(
                Column('password',css_class="form-group col-6"),
                css_class='form-row'
            ),
            Row(
                Column('email',css_class="form-group col-6"),
                css_class="form-row"
            ),
            Submit('submit', 'Sign in')
        )
    class Meta:
        model = User
        fields = [
            'email','username','password',
        ]