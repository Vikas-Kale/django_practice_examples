from django import forms
from django.forms.forms import Form

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile_no = forms.IntegerField()
    Address = forms.CharField()
    