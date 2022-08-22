from django import forms
from .models import Inscription, Content


class ListForm(forms.Form):
    sort = forms.CharField(min_length=1, empty_value='-id')


class ViewForm(forms.Form):
    id = forms.IntegerField(min_value=1)
    key = forms.UUIDField()


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['inscriber', 'title']


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['data']
