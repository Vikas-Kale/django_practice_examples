from django import forms
from django.forms.forms import Form

class RegistrtionForm(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField()
    mobile_number = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)

    