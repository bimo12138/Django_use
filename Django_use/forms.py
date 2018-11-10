from django import forms


class Name(forms.Form):
    name = forms.CharField(min_length=8)