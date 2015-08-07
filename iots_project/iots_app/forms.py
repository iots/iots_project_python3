from django import forms
from django.forms import ModelForm  #for class PushForm
from iots_app.models import PushModel  #for class PushForm

class PushFormAlias(forms.Form):
    msg = forms.CharField(max_length=100)
    url = forms.URLField()

class PushForm(forms.ModelForm):
    class Meta:
        model = PushModel
        fields = '__all__'
