from django import forms
from .models import relativity
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class TheEditor(forms.ModelForm):
    name = "Create"

    title = forms.CharField(
        max_length=50, required=True,
        widget = forms.TextInput(
            attrs= {
                "placeholder":"Here goes title",
            } ) )
    desc = forms.CharField(
        max_length=100, required=True,
        widget = forms.Textarea(
            attrs={
                "placeholder":"Description goes here",
            } ) )
    tech = forms.CharField(
        max_length=50, required=True,
        widget = forms.TextInput(
            attrs={
                "placeholder":"Tech goes here",
            } ) )
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title',css_class="form-group col-6"),
                css_class='form-row'
            ),
            Row(
                Column('tech',css_class="form-group col-6"),
                css_class='form-row'
            ),
            "desc",
            Submit('submit', self.name)
        )

    class Meta:
        model = relativity
        fields = [
            'title','desc','tech'
        ]

class TheEditorUpdater(forms.ModelForm):
    name = "Update"

    title = forms.CharField(
        max_length=50, required=True,
        widget = forms.TextInput(
            attrs= {
                "placeholder":"Here goes title",
            } ) )
    desc = forms.CharField(
        max_length=100, required=True,
        widget = forms.Textarea(
            attrs={
                "placeholder":"Description goes here",
            } ) )
    tech = forms.CharField(
        max_length=50, required=True,
        widget = forms.TextInput(
            attrs={
                "placeholder":"Tech goes here",
            } ) )
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title',css_class="form-group col-6"),
                css_class='form-row'
            ),
            Row(
                Column('tech',css_class="form-group col-6"),
                css_class='form-row'
            ),
            "desc",
            Submit('submit', self.name)
        )

    class Meta:
        model = relativity
        fields = [
            'title','desc','tech'
        ]